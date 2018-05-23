from __future__ import division, print_function
'''
'''

from iotbx.data_manager.miller_array import MillerArrayDataManager
from iotbx.cif_mtz_data_labels import mtz_map_coefficient_labels, \
  cif_map_coefficient_labels

# =============================================================================
class MapCoefficientsDataManager(MillerArrayDataManager):

  datatype = 'map_coefficients'

  # ---------------------------------------------------------------------------
  # Map coefficients

  def add_map_coefficients_phil_str(self):
    '''
    Add custom PHIL and storage for labels
    '''
    return self._add_miller_array_phil_str(MapCoefficientsDataManager.datatype)

  def export_map_coefficients_phil_extract(self):
    '''
    Export custom PHIL extract
    '''
    return self._export_miller_array_phil_extract(
      MapCoefficientsDataManager.datatype)

  def load_map_coefficients_phil_extract(self, phil_extract):
    '''
    Load custom PHIL extract
    '''
    self._load_miller_array_phil_extract(MapCoefficientsDataManager.datatype,
                                         phil_extract)

  def add_map_coefficients(self, filename, data):
    self.add_miller_array(self, filename, data)

  def set_default_map_coefficients(self, filename):
    return self._set_default(MapCoefficientsDataManager.datatype, filename)

  def get_map_coefficients(self, filename=None):
    '''
    Returns the main file object
    '''
    return self._get(MapCoefficientsDataManager.datatype, filename)

  def get_map_coefficients_labels(self, filename=None):
    '''
    Returns a list of array labels
    '''
    return self._get_array_labels(MapCoefficientsDataManager.datatype, filename)

  def get_map_coefficients_arrays(self, labels=None, filename=None):
    '''
    Returns a list of map coefficients from the file
    '''
    return self._get_arrays(MapCoefficientsDataManager.datatype, labels=labels,
                            filename=filename)

  def get_map_coefficients_names(self):
    return self._get_names(MapCoefficientsDataManager.datatype)

  def get_default_map_coefficients_name(self):
    return self._get_default_name(MapCoefficientsDataManager.datatype)

  def remove_map_coefficients(self, filename):
    return self._remove(MapCoefficientsDataManager.datatype, filename)

  def has_map_coefficients(
      self, expected_n=1, exact_count=False, raise_sorry=False):
    return self._has_data(
      MapCoefficientsDataManager.datatype, expected_n=expected_n,
      exact_count=exact_count, raise_sorry=raise_sorry)

  def process_map_coefficients_file(self, filename):
    self.process_miller_array_file(filename)

  def filter_map_coefficients_arrays(self, filename):
    '''
    Populate data structures by checking labels in miller_arrays to determine
    type
    '''
    known_labels = mtz_map_coefficient_labels.union(cif_map_coefficient_labels)
    self._child_filter_arrays(
      MapCoefficientsDataManager.datatype, filename, known_labels)

  def write_map_coefficients_file(
      self, filename, miller_arrays, overwrite=False):
    self.write_miller_array_file(
      filename=filename, miller_arrays=miller_arrays, overwrite=overwrite)

# =============================================================================
# end
