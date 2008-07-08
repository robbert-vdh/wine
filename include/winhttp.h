/*
 * Copyright (C) 2007 Francois Gouget
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#ifndef __WINE_WINHTTP_H
#define __WINE_WINHTTP_H

#define WINHTTPAPI
#define BOOLAPI WINHTTPAPI BOOL WINAPI


typedef LPVOID HINTERNET;
typedef HINTERNET *LPHINTERNET;

#define INTERNET_DEFAULT_PORT           0
#define INTERNET_DEFAULT_HTTP_PORT      80
#define INTERNET_DEFAULT_HTTPS_PORT     443
typedef WORD INTERNET_PORT;
typedef INTERNET_PORT *LPINTERNET_PORT;

#define INTERNET_SCHEME_HTTP            1
#define INTERNET_SCHEME_HTTPS           2
typedef int INTERNET_SCHEME, *LPINTERNET_SCHEME;

/* flags for WinHttpOpen */
#define WINHTTP_FLAG_ASYNC                  0x10000000

/* flags for WinHttpOpenRequest */
#define WINHTTP_FLAG_ESCAPE_PERCENT         0x00000004
#define WINHTTP_FLAG_NULL_CODEPAGE          0x00000008
#define WINHTTP_FLAG_ESCAPE_DISABLE         0x00000040
#define WINHTTP_FLAG_ESCAPE_DISABLE_QUERY   0x00000080
#define WINHTTP_FLAG_BYPASS_PROXY_CACHE     0x00000100
#define WINHTTP_FLAG_REFRESH                WINHTTP_FLAG_BYPASS_PROXY_CACHE
#define WINHTTP_FLAG_SECURE                 0x00800000

#define WINHTTP_ACCESS_TYPE_DEFAULT_PROXY   0
#define WINHTTP_ACCESS_TYPE_NO_PROXY        1
#define WINHTTP_ACCESS_TYPE_NAMED_PROXY     3

#define WINHTTP_NO_PROXY_NAME               NULL
#define WINHTTP_NO_PROXY_BYPASS             NULL

#define WINHTTP_NO_REFERER                  NULL
#define WINHTTP_DEFAULT_ACCEPT_TYPES        NULL

/* flags for WinHttp{Set/Query}Options */
#define WINHTTP_FIRST_OPTION                         WINHTTP_OPTION_CALLBACK
#define WINHTTP_OPTION_CALLBACK                       1
#define WINHTTP_OPTION_RESOLVE_TIMEOUT                2
#define WINHTTP_OPTION_CONNECT_TIMEOUT                3
#define WINHTTP_OPTION_CONNECT_RETRIES                4
#define WINHTTP_OPTION_SEND_TIMEOUT                   5
#define WINHTTP_OPTION_RECEIVE_TIMEOUT                6
#define WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT       7
#define WINHTTP_OPTION_HANDLE_TYPE                    9
#define WINHTTP_OPTION_READ_BUFFER_SIZE              12
#define WINHTTP_OPTION_WRITE_BUFFER_SIZE             13
#define WINHTTP_OPTION_PARENT_HANDLE                 21
#define WINHTTP_OPTION_EXTENDED_ERROR                24
#define WINHTTP_OPTION_SECURITY_FLAGS                31
#define WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT   32
#define WINHTTP_OPTION_URL                           34
#define WINHTTP_OPTION_SECURITY_KEY_BITNESS          36
#define WINHTTP_OPTION_PROXY                         38
#define WINHTTP_OPTION_USER_AGENT                    41
#define WINHTTP_OPTION_CONTEXT_VALUE                 45
#define WINHTTP_OPTION_CLIENT_CERT_CONTEXT           47
#define WINHTTP_OPTION_REQUEST_PRIORITY              58
#define WINHTTP_OPTION_HTTP_VERSION                  59
#define WINHTTP_OPTION_DISABLE_FEATURE               63
#define WINHTTP_OPTION_CODEPAGE                      68
#define WINHTTP_OPTION_MAX_CONNS_PER_SERVER          73
#define WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER      74
#define WINHTTP_OPTION_AUTOLOGON_POLICY              77
#define WINHTTP_OPTION_SERVER_CERT_CONTEXT           78
#define WINHTTP_OPTION_ENABLE_FEATURE                79
#define WINHTTP_OPTION_WORKER_THREAD_COUNT           80
#define WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT      81
#define WINHTTP_OPTION_PASSPORT_COBRANDING_URL       82
#define WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH       83
#define WINHTTP_OPTION_SECURE_PROTOCOLS              84
#define WINHTTP_OPTION_ENABLETRACING                 85
#define WINHTTP_OPTION_PASSPORT_SIGN_OUT             86
#define WINHTTP_OPTION_PASSPORT_RETURN_URL           87
#define WINHTTP_OPTION_REDIRECT_POLICY               88
#define WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS  89
#define WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE      90
#define WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE      91
#define WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE       92
#define WINHTTP_OPTION_CONNECTION_INFO               93
#define WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST       94
#define WINHTTP_OPTION_SPN                           96
#define WINHTTP_OPTION_GLOBAL_PROXY_CREDS            97
#define WINHTTP_OPTION_GLOBAL_SERVER_CREDS           98
#define WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT           99
#define WINHTTP_OPTION_REJECT_USERPWD_IN_URL         100
#define WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS 101
#define WINHTTP_LAST_OPTION                          WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS
#define WINHTTP_OPTION_USERNAME                      0x1000
#define WINHTTP_OPTION_PASSWORD                      0x1001
#define WINHTTP_OPTION_PROXY_USERNAME                0x1002
#define WINHTTP_OPTION_PROXY_PASSWORD                0x1003

/* Options for WinHttpOpenRequest */
#define WINHTTP_NO_REFERER             NULL
#define WINHTTP_DEFAULT_ACCEPT_TYPES   NULL

/* Options for WinHttpSendRequest */
#define WINHTTP_NO_ADDITIONAL_HEADERS   NULL
#define WINHTTP_NO_REQUEST_DATA         NULL

/* WinHTTP error codes */
#define WINHTTP_ERROR_BASE                         12000
#define ERROR_WINHTTP_OUT_OF_HANDLES               (WINHTTP_ERROR_BASE + 1)
#define ERROR_WINHTTP_TIMEOUT                      (WINHTTP_ERROR_BASE + 2)
#define ERROR_WINHTTP_INTERNAL_ERROR               (WINHTTP_ERROR_BASE + 4)
#define ERROR_WINHTTP_INVALID_URL                  (WINHTTP_ERROR_BASE + 5)
#define ERROR_WINHTTP_UNRECOGNIZED_SCHEME          (WINHTTP_ERROR_BASE + 6)
#define ERROR_WINHTTP_NAME_NOT_RESOLVED            (WINHTTP_ERROR_BASE + 7)
#define ERROR_WINHTTP_INVALID_OPTION               (WINHTTP_ERROR_BASE + 9)
#define ERROR_WINHTTP_OPTION_NOT_SETTABLE          (WINHTTP_ERROR_BASE + 11)
#define ERROR_WINHTTP_SHUTDOWN                     (WINHTTP_ERROR_BASE + 12)
#define ERROR_WINHTTP_LOGIN_FAILURE                (WINHTTP_ERROR_BASE + 15)
#define ERROR_WINHTTP_OPERATION_CANCELLED          (WINHTTP_ERROR_BASE + 17)
#define ERROR_WINHTTP_INCORRECT_HANDLE_TYPE        (WINHTTP_ERROR_BASE + 18)
#define ERROR_WINHTTP_INCORRECT_HANDLE_STATE       (WINHTTP_ERROR_BASE + 19)
#define ERROR_WINHTTP_CANNOT_CONNECT               (WINHTTP_ERROR_BASE + 29)
#define ERROR_WINHTTP_CONNECTION_ERROR             (WINHTTP_ERROR_BASE + 30)
#define ERROR_WINHTTP_RESEND_REQUEST               (WINHTTP_ERROR_BASE + 32)
#define ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED      (WINHTTP_ERROR_BASE + 44)
#define ERROR_WINHTTP_CANNOT_CALL_BEFORE_OPEN      (WINHTTP_ERROR_BASE + 100)
#define ERROR_WINHTTP_CANNOT_CALL_BEFORE_SEND      (WINHTTP_ERROR_BASE + 101)
#define ERROR_WINHTTP_CANNOT_CALL_AFTER_SEND       (WINHTTP_ERROR_BASE + 102)
#define ERROR_WINHTTP_CANNOT_CALL_AFTER_OPEN       (WINHTTP_ERROR_BASE + 103)
#define ERROR_WINHTTP_HEADER_NOT_FOUND             (WINHTTP_ERROR_BASE + 150)
#define ERROR_WINHTTP_INVALID_SERVER_RESPONSE      (WINHTTP_ERROR_BASE + 152)
#define ERROR_WINHTTP_INVALID_HEADER               (WINHTTP_ERROR_BASE + 153)
#define ERROR_WINHTTP_INVALID_QUERY_REQUEST        (WINHTTP_ERROR_BASE + 154)
#define ERROR_WINHTTP_HEADER_ALREADY_EXISTS        (WINHTTP_ERROR_BASE + 155)
#define ERROR_WINHTTP_REDIRECT_FAILED              (WINHTTP_ERROR_BASE + 156)
#define ERROR_WINHTTP_BAD_AUTO_PROXY_SCRIPT        (WINHTTP_ERROR_BASE + 166)
#define ERROR_WINHTTP_UNABLE_TO_DOWNLOAD_SCRIPT    (WINHTTP_ERROR_BASE + 167)
#define ERROR_WINHTTP_NOT_INITIALIZED              (WINHTTP_ERROR_BASE + 172)
#define ERROR_WINHTTP_SECURE_FAILURE               (WINHTTP_ERROR_BASE + 175)
#define ERROR_WINHTTP_AUTO_PROXY_SERVICE_ERROR     (WINHTTP_ERROR_BASE + 178)
#define ERROR_WINHTTP_AUTODETECTION_FAILED         (WINHTTP_ERROR_BASE + 180)

typedef struct
{
    DWORD   dwStructSize;
    LPWSTR  lpszScheme;
    DWORD   dwSchemeLength;
    INTERNET_SCHEME nScheme;
    LPWSTR  lpszHostName;
    DWORD   dwHostNameLength;
    INTERNET_PORT nPort;
    LPWSTR  lpszUserName;
    DWORD   dwUserNameLength;
    LPWSTR  lpszPassword;
    DWORD   dwPasswordLength;
    LPWSTR  lpszUrlPath;
    DWORD   dwUrlPathLength;
    LPWSTR  lpszExtraInfo;
    DWORD   dwExtraInfoLength;
} URL_COMPONENTS, *LPURL_COMPONENTS;
typedef URL_COMPONENTS URL_COMPONENTSW;
typedef LPURL_COMPONENTS LPURL_COMPONENTSW;

typedef struct
{
    DWORD_PTR dwResult;
    DWORD dwError;
} WINHTTP_ASYNC_RESULT, *LPWINHTTP_ASYNC_RESULT;

typedef struct
{
    FILETIME ftExpiry;
    FILETIME ftStart;
    LPWSTR lpszSubjectInfo;
    LPWSTR lpszIssuerInfo;
    LPWSTR lpszProtocolName;
    LPWSTR lpszSignatureAlgName;
    LPWSTR lpszEncryptionAlgName;
    DWORD dwKeySize;
} WINHTTP_CERTIFICATE_INFO;

typedef struct
{
    DWORD dwAccessType;
    LPCWSTR lpszProxy;
    LPCWSTR lpszProxyBypass;
} WINHTTP_PROXY_INFO, *LPWINHTTP_PROXY_INFO;
typedef WINHTTP_PROXY_INFO WINHTTP_PROXY_INFOW;
typedef LPWINHTTP_PROXY_INFO LPWINHTTP_PROXY_INFOW;

typedef struct
{
    BOOL   fAutoDetect;
    LPWSTR lpszAutoConfigUrl;
    LPWSTR lpszProxy;
    LPWSTR lpszProxyBypass;
} WINHTTP_CURRENT_USER_IE_PROXY_CONFIG;

typedef VOID (CALLBACK *WINHTTP_STATUS_CALLBACK)(HINTERNET,DWORD_PTR,DWORD,LPVOID,DWORD);

typedef struct
{
    DWORD dwFlags;
    DWORD dwAutoDetectFlags;
    LPCWSTR lpszAutoConfigUrl;
    LPVOID lpvReserved;
    DWORD dwReserved;
    BOOL fAutoLogonIfChallenged;
} WINHTTP_AUTOPROXY_OPTIONS;

typedef struct
{
    DWORD dwMajorVersion;
    DWORD dwMinorVersion;
} HTTP_VERSION_INFO, *LPHTTP_VERSION_INFO;


#ifdef __cplusplus
extern "C" {
#endif

BOOL        WINAPI WinHttpAddRequestHeaders(HINTERNET,LPCWSTR,DWORD,DWORD);
BOOL        WINAPI WinHttpDetectAutoProxyConfigUrl(DWORD,LPWSTR*);
BOOL        WINAPI WinHttpCheckPlatform(void);
BOOL        WINAPI WinHttpCloseHandle(HINTERNET);
HINTERNET   WINAPI WinHttpConnect(HINTERNET,LPCWSTR,INTERNET_PORT,DWORD);
BOOL        WINAPI WinHttpCrackUrl(LPCWSTR,DWORD,DWORD,LPURL_COMPONENTS);
BOOL        WINAPI WinHttpCreateUrl(LPURL_COMPONENTS,DWORD,LPWSTR,LPDWORD);
BOOL        WINAPI WinHttpGetDefaultProxyConfiguration(WINHTTP_PROXY_INFO*);
BOOL        WINAPI WinHttpGetIEProxyConfigForCurrentUser(WINHTTP_CURRENT_USER_IE_PROXY_CONFIG* config);
BOOL        WINAPI WinHttpGetProxyForUrl(HINTERNET,LPCWSTR,WINHTTP_AUTOPROXY_OPTIONS*,WINHTTP_PROXY_INFO*);
HINTERNET   WINAPI WinHttpOpen(LPCWSTR,DWORD,LPCWSTR,LPCWSTR,DWORD);
HINTERNET   WINAPI WinHttpOpenRequest(HINTERNET,LPCWSTR,LPCWSTR,LPCWSTR,LPCWSTR,LPCWSTR*,DWORD);
BOOL        WINAPI WinHttpQueryAuthParams(HINTERNET,DWORD,LPVOID*);
BOOL        WINAPI WinHttpQueryAuthSchemes(HINTERNET,LPDWORD,LPDWORD,LPDWORD);
BOOL        WINAPI WinHttpQueryDataAvailable(HINTERNET,LPDWORD);
BOOL        WINAPI WinHttpQueryHeaders(HINTERNET,DWORD,LPCWSTR,LPVOID,LPDWORD,LPDWORD);
BOOL        WINAPI WinHttpReadData(HINTERNET,LPVOID,DWORD,LPDWORD);
BOOL        WINAPI WinHttpReceiveResponse(HINTERNET,LPVOID);
BOOL        WINAPI WinHttpSendRequest(HINTERNET,LPCWSTR,DWORD,LPVOID,DWORD,DWORD,DWORD_PTR);
BOOL        WINAPI WinHttpSetDefaultProxyConfiguration(WINHTTP_PROXY_INFO*);
BOOL        WINAPI WinHttpSetCredentials(HINTERNET,DWORD,DWORD,LPCWSTR,LPCWSTR,LPVOID);
BOOL        WINAPI WinHttpSetOption(HINTERNET,DWORD,LPVOID,DWORD);
WINHTTP_STATUS_CALLBACK WINAPI WinHttpSetStatusCallback(HINTERNET,WINHTTP_STATUS_CALLBACK,DWORD,DWORD_PTR);
BOOL        WINAPI WinHttpSetTimeouts(HINTERNET,int,int,int,int);
BOOL        WINAPI WinHttpTimeFromSystemTime(CONST SYSTEMTIME *,LPWSTR);
BOOL        WINAPI WinHttpTimeToSystemTime(LPCWSTR,SYSTEMTIME*);
BOOL        WINAPI WinHttpWriteData(HINTERNET,LPCVOID,DWORD,LPDWORD);

#ifdef __cplusplus
}
#endif

#endif  /* __WINE_WINHTTP_H */
