from __future__ import division
#import sys
import math
from cctbx import geometry_restraints
#from libtbx.utils import Sorry
#from scitbx import matrix
from scitbx.array_family import flex
from scitbx.math import dihedral_angle

class neighbors(object):
  def __init__(self,
      ih = None,
      a0 = {},
      a1 = {},
      a2 = {},
      a3 = {},
      h1 = {},
      h2 = {},
      b1 = {},
      number_h_neighbors = None,
      number_non_h_neighbors = None):
    self.ih = ih
    self.a0 = a0
    self.a1 = a1
    self.a2 = a2
    self.a3 = a3
    self.h1 = h1
    self.h2 = h2
    self.b1 = b1
    self.number_h_neighbors = number_h_neighbors
    self.number_non_h_neighbors = number_non_h_neighbors

class determine_connectivity(object):
  """ Obtain information about the necessary number of neighbors to reconstruct
  the position of every H atom ("connectivity") and to determine the geometry
  of the H atom. Store also information about ideal angles involving H atom,
  and non-H atoms as well as dihedral angle
  :returns: an array of "neighbors" objects (defined above)
  :rtype: list[]"""
  def __init__(self,
      pdb_hierarchy,
      geometry_restraints):
    self.pdb_hierarchy = pdb_hierarchy
    self.geometry_restraints = geometry_restraints
    self.atoms = self.pdb_hierarchy.atoms()
    self.sites_cart = self.atoms.extract_xyz()
    self.bond_proxies_simple, self.asu = \
      self.geometry_restraints.get_all_bond_proxies(sites_cart=self.sites_cart)
    self.angle_proxies = self.geometry_restraints.get_all_angle_proxies()
    self.dihedral_proxies = self.geometry_restraints.dihedral_proxies # this should be function in GRM, like previous
    self.fsc0 = \
      self.geometry_restraints.shell_sym_tables[0].full_simple_connectivity()
    self.n_atoms = self.pdb_hierarchy.atoms_size()
    self.hd_sel = self.hd_selection()
    # self.h_connectivity = [None for i in range(self.n_atoms)]
    # ~7 times faster:
    self.h_connectivity = [None]*self.n_atoms
    self.names = list(self.atoms.extract_name())

    # 1. make empty list for h_connectivity
    # self.initialize_connectivity() - one liner used once is a bit excessive

    # 2. find parent atoms and ideal A0-H bond distances
    self.find_first_neighbors()
    # Check that H atoms in connectivity and total number of H atoms is the same
    self.count_H()
    # 3. find preliminary list of second neighbors
    self.find_second_neighbors_raw()

    # 4. process preliminary list to eliminate atoms in double conformation
    self.process_second_neighbors()

    # 5. Find third neighbors via dihedral proxies
    self.find_third_neighbors()

    # 6. Find angles involving a0 and covalently bound non-H atoms
    # also: find preliminary list of third neighbors in cases where no dihedral
    # proxy is present
    self.determine_a0_angles_and_third_neighbors_without_dihedral()

    # 7. assign the angles found previously and process preliminary list of
    # third neighbors
    self.process_a0_angles_and_third_neighbors_without_dihedral()

    #self.print_stuff()


  def find_first_neighbors(self):
    """ Find first neighbors by looping through bond proxies
    Fills in dictionary of 'a0' in object 'neighbors'.
    Keys: i_seq, dist_ideal"""
    self.double_H = {}
    self.parents = set()
    for bproxy in self.bond_proxies_simple:
      i_seq, j_seq = bproxy.i_seqs
      is_i_hd = self.hd_sel[i_seq]
      is_j_hd = self.hd_sel[j_seq]
      if(not is_i_hd and not is_j_hd): continue
      elif(is_i_hd and is_j_hd):       assert 0
      else:
        if  (is_i_hd): ih, i_parent = i_seq, j_seq
        elif(is_j_hd): ih, i_parent = j_seq, i_seq
        # else case should not happen...
        #else:
        #  raise Sorry("Something went wrong in bond proxies")
      # if neighbor exists, use only first one found
      if self.h_connectivity[ih] is not None: continue
      # find H atoms bound to two parent atoms, store info in list 'double_H'
      if (self.fsc0[ih].size() > 1):
        self.double_H[ih] = list(self.fsc0[ih])
      self.h_connectivity[ih] = neighbors(
        ih = ih,
        a0 = {'iseq':i_parent, 'dist_ideal': bproxy.distance_ideal,
          'angles':[]})
      self.parents.add(i_parent) #list of parent atoms

  def find_second_neighbors_raw(self):
    """Get a an array listing all second neighbors for every H atom.
    :returns: an array containing lists: [[iseq1, iseq2, ...], ...]
    :rtype: [[],[].[]]
    """
    self.second_neighbors_raw = [[] for i in range(self.n_atoms)]
    self.angle_dict = {}
    for ap in self.angle_proxies:
      for i_test in ap.i_seqs:
        if (self.h_connectivity[i_test] is None and not self.hd_sel[i_test]):
          continue
        ih = i_test
        i_parent = ap.i_seqs[1]
        # if one H bound to two parents (case double_H)
        if (i_parent not in self.parents): continue
        bonded = [ih, i_parent]
        i_second = [x for x in ap.i_seqs if x not in bonded][0]
        assert(self.h_connectivity[ih].a0['iseq'] == i_parent)
        self.second_neighbors_raw[ih].append(i_second)
        self.angle_dict[(ih, i_parent, i_second)] = ap.angle_ideal

  def process_second_neighbors(self):
    """Once canditades for second neighbors are determined, they are further
    processed, mainly to avoid alternative conformations of the same atom"""
    self.a0a1_dict = {}
    self.a1_atoms = set()
    for neighbors in self.h_connectivity:
      if (neighbors is None): continue
      ih = neighbors.ih
      i_parent = neighbors.a0['iseq']
      second_neighbors_reduced = []
      alt_conf_neighbors = []
      for i_second in self.second_neighbors_raw[ih]:
        altloc_i_second = self.atoms[i_second].parent().altloc
        if (altloc_i_second == ''):
          second_neighbors_reduced.append(i_second)
        else:
          alt_conf_neighbors.append(i_second)
      second_neighbors_reduced.extend(self.process_alternate_neighbors(
        alt_conf_neighbors = alt_conf_neighbors))
      second_neighbors_H = self.determine_second_neighbors_H(
        second_neighbors_reduced = second_neighbors_reduced)
      second_neighbors_non_H = list(
        set(second_neighbors_reduced) - set(second_neighbors_H))
      self.assign_second_neighbors(
        ih               = ih,
        i_parent         = i_parent,
        neighbors_list   = second_neighbors_non_H,
        neighbors_list_H = second_neighbors_H)
      if (neighbors.number_non_h_neighbors == 1):
        i_a1 = self.h_connectivity[ih].a1['iseq']
        self.a1_atoms.add(i_a1)
        self.a0a1_dict[i_parent] = i_a1

  def print_stuff(self):
    """Print information of connectivity for each H atom."""
    for neighbors in self.h_connectivity:
      if neighbors is None: continue
      ih = neighbors.ih
      labels = self.atoms[ih].fetch_labels()
      i_a0 = neighbors.a0['iseq']
      i_a1 = neighbors.a1['iseq']
      string = self.names[i_a1]+'('+str(i_a1)+')'
      if 'iseq' in neighbors.a2:
        i_a2 = neighbors.a2['iseq']
        string = string + self.names[i_a2]
      if 'iseq' in neighbors.a3:
        string = string + self.names[neighbors.a3['iseq']]
      output = (self.names[ih], ih, labels.resseq.strip(), self.names[i_a0], i_a0, string)
      stringh = ''
      if 'iseq' in neighbors.h1:
        stringh = stringh + self.names[neighbors.h1['iseq']]
      if 'iseq' in neighbors.h2:
        stringh = stringh + self.names[neighbors.h2['iseq']]
      if 'iseq' in neighbors.b1:
        stringb1 = self.names[neighbors.b1['iseq']]
      else:
        stringb1 = 'n/a'
      output = output + (stringh,) + (stringb1,)#+ (self.third_neighbors_raw[i_a0],)
      print '%s %s (%s) , %s (%s) , %s , %s,%s' % output

  def determine_a0_angles_and_third_neighbors_without_dihedral(self):
    """Loop through angle proxies to find angles involving a0 and second
    neighbors. Find raw list of third neighbors, which don't have dihedral
    proxies."""
    self.parent_angles = [{} for i in range(self.n_atoms)]
    self.third_neighbors_raw = [[] for i in range(self.n_atoms)]
    for ap in self.angle_proxies:
      ix, iy, iz = ap.i_seqs
      is_hd_ix = self.hd_sel[ix]
      is_hd_iz = self.hd_sel[iz]
      labels = self.atoms[iy].fetch_labels()
      # get all X1-A0-X2 angles if A0 is parent atom
      if (iy in self.parents and not is_hd_ix and not is_hd_iz):
          self.parent_angles[iy][(ix, iz)] = ap.angle_ideal
      # for third neighbors, a1 atom is central
      if (is_hd_ix or is_hd_iz): continue
      if (iy in self.a1_atoms):
        if (ix in self.parents and ix in self.a0a1_dict):
          if (self.a0a1_dict[ix]==iy and not is_hd_iz):
            i_parent = ix
            i_third = iz
        elif (iz in self.parents and iz in self.a0a1_dict):
          if (self.a0a1_dict[iz]==iy and not is_hd_ix):
            i_parent = iz
            i_third = ix
        else:
          continue
        if (i_third not in self.third_neighbors_raw[i_parent]):
          self.third_neighbors_raw[i_parent].append(i_third)
          if (i_third in self.parents):
            self.third_neighbors_raw[i_third].append(i_parent)

  def process_a0_angles_and_third_neighbors_without_dihedral(self):
    """Process raw list of third neighbors withouth ideal dihedral proxy."""
    for neighbors in self.h_connectivity:
      if (neighbors is None): continue
      ih = neighbors.ih
      i_parent = neighbors.a0['iseq']
      self.assign_a0_angles(ih = ih)
      if (neighbors.number_non_h_neighbors != 1 or 'iseq' in neighbors.b1):
        continue
      third_neighbors = self.third_neighbors_raw[i_parent]
      third_neighbors_reduced = []
      alt_conf_neighbors = []
      for i_third in third_neighbors:
        altloc_i_third = self.atoms[i_third].parent().altloc
        if (altloc_i_third == ''):
          third_neighbors_reduced.append(i_third)
        else:
          alt_conf_neighbors.append(i_third)
      third_neighbors_reduced.extend(self.process_alternate_neighbors(
        alt_conf_neighbors = alt_conf_neighbors))
      # If there is no dihedral ideal angle, use randomly first atom
      # in list of third neighbors
      self.h_connectivity[ih].b1 = {'iseq': third_neighbors_reduced[0]}


  def assign_a0_angles(self, ih):
    """ Having a list of dictionaries for the angles involving atom a0,
    assign the angles to the correct set of three atoms. """
    neighbors = self.h_connectivity[ih]
    if (neighbors.number_non_h_neighbors > 1):
      a0_iseq = neighbors.a0['iseq']
      a1_iseq = neighbors.a1['iseq']
      a2_iseq = neighbors.a2['iseq']
      if (a1_iseq, a2_iseq) in self.parent_angles[a0_iseq]:
        self.h_connectivity[ih].a0['angle_a1a0a2'] = \
          self.parent_angles[a0_iseq][(a1_iseq, a2_iseq)]
      elif (a2_iseq, a1_iseq) in self.parent_angles[a0_iseq]:
        self.h_connectivity[ih].a0['angle_a1a0a2'] = \
          self.parent_angles[a0_iseq][(a2_iseq, a1_iseq)]
      else:
        print 'something went wrong'
      if (neighbors.number_non_h_neighbors == 3):
        a3_iseq = neighbors.a3['iseq']
        if (a2_iseq, a3_iseq) in self.parent_angles[a0_iseq]:
          self.h_connectivity[ih].a0['angle_a2a0a3'] = \
            self.parent_angles[a0_iseq][(a2_iseq, a3_iseq)]
        elif (a3_iseq, a2_iseq) in self.parent_angles[a0_iseq]:
          self.h_connectivity[ih].a0['angle_a2a0a3'] = \
            self.parent_angles[a0_iseq][(a3_iseq, a2_iseq)]
        if (a3_iseq, a1_iseq) in self.parent_angles[a0_iseq]:
          self.h_connectivity[ih].a0['angle_a3a0a1'] = \
            self.parent_angles[a0_iseq][(a3_iseq, a1_iseq)]
        elif (a1_iseq, a3_iseq) in self.parent_angles[a0_iseq]:
          self.h_connectivity[ih].a0['angle_a3a0a1'] = \
            self.parent_angles[a0_iseq][(a1_iseq, a3_iseq)]
        else:
          print 'something went wrong'

  def find_third_neighbors(self):
    """ Loop through dihedral angle proxies to find third neighbor
    Fill in neighbors.b1 with iseq and angle proxy"""
    for dp in self.dihedral_proxies:
      for i_test in dp.i_seqs:
        if (self.h_connectivity[i_test] is None and not self.hd_sel[i_test]):
          continue
        ih = i_test
        i1, i2, i3, i4 = dp.i_seqs
        if (ih == i1):
          i_third = i4
        if (ih == i4):
          i_third = i1
        dihedral = dihedral_angle(
              sites = [self.sites_cart[i1], self.sites_cart[i2],
              self.sites_cart[i3],self.sites_cart[i4]])
        dihedral_id = dp.angle_ideal
        delta = geometry_restraints.angle_delta_deg(
          angle_1 = math.degrees(dihedral),
          angle_2 = dihedral_id,
          periodicity = dp.periodicity)
        dihedral_ideal = math.degrees(dihedral) + delta
        b1 = {'iseq': i_third, 'dihedral_ideal': dihedral_ideal}
        self.h_connectivity[ih].b1 = b1
        self.assign_b1_for_H_atom_groups(ih = ih, i_third = i_third)

  def assign_b1_for_H_atom_groups(self, ih, i_third):
    """ For atom groups (such as propeller), only one H atom has dihedral proxy
    For the other H atoms of such groups, fill in only iseq"""
    number_h_neighbors = self.h_connectivity[ih].number_h_neighbors
    if (number_h_neighbors > 0):
      i_h1 = self.h_connectivity[ih].h1['iseq']
      self.h_connectivity[i_h1].b1 = {'iseq': i_third}
      if (number_h_neighbors == 2):
        i_h2 = self.h_connectivity[ih].h2['iseq']
        self.h_connectivity[i_h2].b1 = {'iseq': i_third}

  def determine_second_neighbors_H(self, second_neighbors_reduced):
    """Determine if there are H atoms among second neighbors and store them
    in a list 'second_neighbors_H' """
    second_neighbors_H = []
    for iseq in second_neighbors_reduced:
      if (self.hd_sel[iseq]):
        second_neighbors_H.append(iseq)
    return second_neighbors_H

  def assign_second_neighbors(
          self, ih, i_parent, neighbors_list, neighbors_list_H):
    """With the information of second neighbors, fill in the dictionaries for
    each atom (a1, a2, a3, according to which is present)."""
    number_h_neighbors = 0
    number_non_h_neighbors = 0
    for iseq, n in zip(neighbors_list, [1,2,3]):
      number_non_h_neighbors = number_non_h_neighbors + 1
      a = self.make_neighbor_dict(iseq = iseq, ih = ih, i_parent = i_parent)
      if (n == 1): self.h_connectivity[ih].a1 = a
      if (n == 2): self.h_connectivity[ih].a2 = a
      if (n == 3): self.h_connectivity[ih].a3 = a
    for iseqh, nh in zip(neighbors_list_H, [1,2]):
      number_h_neighbors = number_h_neighbors + 1
      ah = self.make_neighbor_dict(iseq = iseqh, ih = ih, i_parent = i_parent)
      if (nh == 1): self.h_connectivity[ih].h1 = ah
      if (nh == 2): self.h_connectivity[ih].h2 = ah
    self.h_connectivity[ih].number_h_neighbors = number_h_neighbors
    self.h_connectivity[ih].number_non_h_neighbors = number_non_h_neighbors

  def make_neighbor_dict(self, iseq, ih, i_parent):
    angle = self.angle_dict[(ih, i_parent, iseq)]
    neighbor = {'iseq': iseq, 'angle_ideal': angle}
    return neighbor

  def process_alternate_neighbors(self, alt_conf_neighbors):
    """ For a list of atoms in alternative conformations, retain singles and
    those with higher occupancy
    Example: [CA-A, N-A, N-B] --> [CA-A, N-B] if occ(N-B) > occ(N-A)"""
    alt_conf_neighbors_temp = []
    alt_conf_neighbors_reduced = []
    # if only one atom in alt conf list, not necessary to search for other atoms
    if (len(alt_conf_neighbors) == 1):
      alt_conf_neighbors_reduced.append(alt_conf_neighbors[0])
    # Go through each atom in dc, get the name and make temporary dictionary
    # with iseq as key which points to occupancy: {i_1:occA, i_2:occB, i_3:occC}
    # Then choose atom with maximum occupancy
    else:
      for i_second in alt_conf_neighbors:
        altloc_dict_temp = {}
        if (i_second in alt_conf_neighbors_temp): continue
        name_i_second = self.atoms[i_second].name
        altloc_i_second = self.atoms[i_second].parent().altloc
        # check if all neighbors are in the same alt conf (otherwise no angle proxy)
        if alt_conf_neighbors_reduced:
          i_previous = alt_conf_neighbors_reduced[0]
          altloc_previous = self.atoms[i_previous].parent().altloc
          if (altloc_i_second != altloc_previous):
            alt_conf_neighbors_temp.append(i_second)
            continue
        altloc_dict_temp[i_second] = self.atoms[i_second].occ
        for ag in self.atoms[i_second].parent().parent().atom_groups():
          for ag_atom in ag.atoms():
            if (ag_atom.i_seq == altloc_i_second): continue
            if (ag_atom.i_seq in alt_conf_neighbors_temp): continue
            if (ag_atom.name == name_i_second and
                ag_atom.i_seq in alt_conf_neighbors):
              altloc_dict_temp[ag_atom.i_seq] = ag_atom.occ
        i_second_max = max(altloc_dict_temp, key=lambda k: altloc_dict_temp[k])
        alt_conf_neighbors_reduced.append(i_second_max)
        # Store "used" atoms in temp list --> avoids going through atoms twice
        for index in altloc_dict_temp.keys():
          alt_conf_neighbors_temp.append(index)
    return alt_conf_neighbors_reduced


  # def initialize_connectivity(self):
  #   """Get a an array for all scatterers of the structure.
  #   :returns: an array containing None for every atom
  #   :rtype: []
  #   """
  #   self.h_connectivity = [None for i in range(self.n_atoms)]

  def count_H(self):
    """# Check if number H/D atoms in the hd_selection (= in the model) and
    in h_connectivity are the same"""
    number_h_1 = 0
    for h_bool in self.hd_sel:
      # what about short notation to look nicer?:
      if h_bool: number_h_1 += 1
    number_h_2 = 0
    for item in self.h_connectivity:
      if item: number_h_2 = number_h_2 + 1
    assert (number_h_1 == number_h_2)

  def hd_selection(self):
    """Get a selector array for all hydrogen and deuterium scatterers of the structure.
    :returns: an array to select all H and D scatterers of the structure
    :rtype: boolean[]
    """
    # looked very much like copy-paste from xray structure
    # (cctbx_project/cctbx/xray/structure.py) - which is fine, but
    # As a general function it should reside in
    # cctbx_project/iotbx/pdb/hierarchy.py as pdb_hierarchy method
    # Surprisingly, append() here works bit faster than making the correct
    # size array and access by elements...

    result = flex.bool()
    for atom in (self.pdb_hierarchy.atoms()):
      result.append(atom.element_is_hydrogen())
    return result

  # This function is not used anywhere, probably this is the reason it
  # does not generate syntax error (missing self)
  # def is_same_element(iseq1, iseq2, atoms):
  #   """Get a boolean if atom iseq1 and iseq2 have the same element.
  #   :returns: a boolean value
  #   :rtype: boolean
  #   """
  #   if (atoms[iseq1].element == atoms[iseq2].element):
  #     result = True
  #   else:
  #     result =False
  #   return result
