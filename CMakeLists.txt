cmake_minimum_required(VERSION 3.13.4)

project(UpperAirwaySegmentator)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/alejandro-matos/SlicerUpperAirwaySegmentator")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Alejandro Matos Camarillo (uAlberta), Silvia Capenakas (uAlberta)")
set(EXTENSION_DESCRIPTION "Fully automatic AI segmentation tool for upper airway CBCT scans based on UpperAirwaySegmentator nnU-Net model.")
# tk add ICONURL
set(EXTENSION_ICONURL "https://github.com/gaudot/SlicerDentalSegmentator/raw/main/DentalSegmentator/Resources/Icons/DentalSegmentator_full_icon.png")
# tk add screenshot
set(EXTENSION_SCREENSHOTURLS "https://github.com/gaudot/SlicerDentalSegmentator/raw/main/Screenshots/1.png")
set(EXTENSION_DEPENDS "NNUNet") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(UpperAirwaySegmentator)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
