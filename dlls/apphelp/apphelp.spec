@ stub AllowPermLayer
@ stub ApphelpCheckExe
@ stdcall ApphelpCheckInstallShieldPackage(ptr wstr)
@ stdcall ApphelpCheckMsiPackage(ptr wstr)
@ stub ApphelpCheckRunApp
@ stub ApphelpCheckRunAppEx
@ stdcall ApphelpCheckShellObject(ptr long ptr)
@ stub ApphelpCreateAppcompatData
@ stub ApphelpFixMsiPackage
@ stub ApphelpFixMsiPackageExe
@ stub ApphelpFreeFileAttributes
@ stub ApphelpGetFileAttributes
@ stub ApphelpGetMsiProperties
@ stub ApphelpGetNTVDMInfo
@ stub ApphelpParseModuleData
@ stub ApphelpQueryModuleData
@ stub ApphelpQueryModuleDataEx
@ stub ApphelpUpdateCacheEntry
@ stub GetPermLayers
@ stub SE_DllLoaded
@ stub SE_DllUnloaded
@ stub SE_GetHookAPIs
@ stub SE_GetMaxShimCount
@ stub SE_GetProcAddressLoad
@ stub SE_GetShimCount
@ stub SE_InstallAfterInit
@ stub SE_InstallBeforeInit
@ stub SE_IsShimDll
@ stub SE_LdrEntryRemoved
@ stub SE_ProcessDying
@ stub SdbAddLayerTagRefToQuery
@ stub SdbApphelpNotify
@ stub SdbApphelpNotifyExSdbApphelpNotifyEx
@ stub SdbBuildCompatEnvVariables
@ stub SdbCloseApphelpInformation
@ stdcall SdbCloseDatabase(ptr)
@ stub SdbCloseDatabaseWrite
@ stub SdbCloseLocalDatabase
@ stub SdbCommitIndexes
@ stdcall SdbCreateDatabase(wstr long)
@ stub SdbCreateHelpCenterURL
@ stub SdbCreateMsiTransformFile
@ stub SdbDeclareIndex
@ stub SdbDumpSearchPathPartCaches
@ stub SdbEnumMsiTransforms
@ stub SdbEscapeApphelpURL
@ stub SdbFindFirstDWORDIndexedTag
@ stub SdbFindFirstMsiPackage
@ stub SdbFindFirstMsiPackage_Str
@ stub SdbFindFirstNamedTag
@ stub SdbFindFirstStringIndexedTag
@ stub SdbFindFirstTag
@ stub SdbFindFirstTagRef
@ stub SdbFindNextDWORDIndexedTag
@ stub SdbFindNextMsiPackage
@ stub SdbFindNextStringIndexedTag
@ stub SdbFindNextTag
@ stub SdbFindNextTagRef
@ stub SdbFreeDatabaseInformation
@ stub SdbFreeFileInfo
@ stub SdbFreeFlagInfo
@ stub SdbGUIDFromString
@ stub SdbGUIDToString
@ stub SdbGetAppCompatDataSize
@ stdcall SdbGetAppPatchDir(long ptr long)
@ stub SdbGetBinaryTagData
@ stub SdbGetDatabaseID
@ stub SdbGetDatabaseInformation
@ stub SdbGetDatabaseInformationByName
@ stub SdbGetDatabaseMatch
@ stub SdbGetDatabaseVersion
@ stub SdbGetDllPath
@ stub SdbGetEntryFlags
@ stub SdbGetFileAttributes
@ stub SdbGetFileImageType
@ stub SdbGetFileImageTypeEx
@ stub SdbGetFileInfo
@ stdcall SdbGetFirstChild(ptr long)
@ stub SdbGetIndex
@ stub SdbGetItemFromItemRef
@ stub SdbGetLayerName
@ stub SdbGetLayerTagRef
@ stub SdbGetLocalPDB
@ stub SdbGetMatchingExe
@ stub SdbGetMsiPackageInformation
@ stub SdbGetNamedLayer
@ stub SdbGetNextChild
@ stub SdbGetNthUserSdb
@ stdcall SdbGetPermLayerKeys(wstr ptr ptr long)
@ stub SdbGetShowDebugInfoOption
@ stub SdbGetShowDebugInfoOptionValue
@ stub SdbGetStandardDatabaseGUID
@ stub SdbGetStringTagPtr
@ stub SdbGetTagFromTagID
@ stub SdbGrabMatchingInfo
@ stub SdbGrabMatchingInfoEx
@ stdcall SdbInitDatabase(long wstr)
@ stub SdbInitDatabaseEx
@ stub SdbIsNullGUID
@ stub SdbIsStandardDatabase
@ stub SdbIsTagrefFromLocalDB
@ stub SdbIsTagrefFromMainDB
@ stub SdbLoadString
@ stub SdbMakeIndexKeyFromString
@ stub SdbOpenApphelpDetailsDatabase
@ stub SdbOpenApphelpDetailsDatabaseSP
@ stub SdbOpenApphelpInformation
@ stub SdbOpenApphelpInformationByID
@ stub SdbOpenApphelpResourceFile
@ stdcall SdbOpenDatabase(wstr long)
@ stub SdbOpenDbFromGuid
@ stub SdbOpenLocalDatabase
@ stub SdbPackAppCompatData
@ stub SdbQueryApphelpInformation
@ stub SdbQueryBlockUpgrade
@ stub SdbQueryContext
@ stub SdbQueryData
@ stub SdbQueryDataEx
@ stub SdbQueryDataExTagID
@ stub SdbQueryFlagInfo
@ stub SdbQueryName
@ stub SdbQueryReinstallUpgrade
@ stub SdbReadApphelpData
@ stub SdbReadApphelpDetailsData
@ stub SdbReadBYTETag
@ stub SdbReadBinaryTag
@ stub SdbReadDWORDTagRef
@ stub SdbReadEntryInformation
@ stub SdbReadMsiTransformInfo
@ stub SdbReadPatchBits
@ stub SdbReadQWORDTag
@ stub SdbReadQWORDTagRef
@ stub SdbReadStringTag
@ stub SdbReadStringTagRef
@ stub SdbReadWORDTagRef
@ stub SdbRegisterDatabase
@ stub SdbReleaseDatabase
@ stub SdbReleaseMatchingExe
@ stub SdbResolveDatabase
@ stub SdbSetApphelpDebugParameters
@ stub SdbSetEntryFlags
@ stub SdbSetImageType
@ stdcall SdbSetPermLayerKeys(wstr wstr long)
@ stub SdbShowApphelpDialog
@ stub SdbShowApphelpFromQuery
@ stub SdbStartIndexing
@ stub SdbStopIndexing
@ stub SdbStringDuplicate
@ stub SdbStringReplace
@ stub SdbStringReplaceArray
@ stub SdbTagIDToTagRef
@ stub SdbTagToString
@ stub SdbUnregisterDatabase
@ stub SdbWriteBYTETag
@ stub SdbWriteBinaryTag
@ stub SdbWriteBinaryTagFromFile
@ stub SdbWriteDWORDTag
@ stub SdbWriteNULLTag
@ stub SdbWriteQWORDTag
@ stub SdbWriteStringRefTag
@ stub SdbWriteStringTag
@ stub SdbWriteStringTagDirect
@ stub SdbWriteWORDTag
@ stdcall SetPermLayerState(wstr ptr ptr long long)
@ stub SetPermLayers
@ stub ShimDbgPrint
@ stub ShimDumpCache
@ stdcall ShimFlushCache(ptr ptr str long)
