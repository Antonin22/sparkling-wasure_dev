SET(CRITERION_INCLUDE_DIR ${EXTERN_PROJECT_SRC_DIR}/Criterion/include)

FIND_LIBRARY(CRITERION_LIBRARIES libcriterion.so
  ${EXTERN_PROJECT_SRC_DIR}/Criterion/build-Release/
  ${EXTERN_PROJECT_SRC_DIR}/Criterion/build-Debug/
)

IF (CRITERION_INCLUDE_DIR)
  SET(CRITERION_INCLUDE_FOUND "YES")
  MESSAGE(STATUS "Found CRITERION include dir: ${CRITERION_INCLUDE_DIR}")
ELSE(CRITERION_INCLUDE_DIR)
 MESSAGE(STATUS "/!\ /!\ Not Found : CRITERION include dir ")
ENDIF (CRITERION_INCLUDE_DIR)

IF (CRITERION_LIBRARIES)
  SET(CRITERION_LIB_FOUND "YES")
  MESSAGE(STATUS "Found CRITERION lib: ${CRITERION_LIBRARIES}")
ELSE(CRITERION_LIBRARIES) 
 MESSAGE(STATUS "/!\ /!\ Not Found : CRITERION libs")
ENDIF (CRITERION_LIBRARIES)


IF(CRITERION_LIB_FOUND AND CRITERION_INCLUDE_FOUND)
  SET(CRITERION_FOUND "YES")
ENDIF(CRITERION_LIB_FOUND AND CRITERION_INCLUDE_FOUND)
