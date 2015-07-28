#!/usr/bin/env python

from gentokenlookup import gentokenlookup

OPTIONS = [
    "private-key-file",
    "private-key-passwd-file",
    "certificate-file",
    "dh-param-file",
    "subcert",
    "backend",
    "frontend",
    "workers",
    "http2-max-concurrent-streams",
    "log-level",
    "daemon",
    "http2-proxy",
    "http2-bridge",
    "client-proxy",
    "add-x-forwarded-for",
    "strip-incoming-x-forwarded-for",
    "no-via",
    "frontend-http2-read-timeout",
    "frontend-read-timeout",
    "frontend-write-timeout",
    "backend-read-timeout",
    "backend-write-timeout",
    "stream-read-timeout",
    "stream-write-timeout",
    "accesslog-file",
    "accesslog-syslog",
    "accesslog-format",
    "errorlog-file",
    "errorlog-syslog",
    "backend-keep-alive-timeout",
    "frontend-http2-window-bits",
    "backend-http2-window-bits",
    "frontend-http2-connection-window-bits",
    "backend-http2-connection-window-bits",
    "frontend-no-tls",
    "backend-no-tls",
    "backend-tls-sni-field",
    "pid-file",
    "user",
    "syslog-facility",
    "backlog",
    "ciphers",
    "client",
    "insecure",
    "cacert",
    "backend-ipv4",
    "backend-ipv6",
    "backend-http-proxy-uri",
    "read-rate",
    "read-burst",
    "write-rate",
    "write-burst",
    "worker-read-rate",
    "worker-read-burst",
    "worker-write-rate",
    "worker-write-burst",
    "npn-list",
    "tls-proto-list",
    "verify-client",
    "verify-client-cacert",
    "client-private-key-file",
    "client-cert-file",
    "frontend-http2-dump-request-header",
    "frontend-http2-dump-response-header",
    "http2-no-cookie-crumbling",
    "frontend-frame-debug",
    "padding",
    "altsvc",
    "add-request-header",
    "add-response-header",
    "worker-frontend-connections",
    "no-location-rewrite",
    "no-host-rewrite",
    "backend-http1-connections-per-host",
    "backend-http1-connections-per-frontend",
    "listener-disable-timeout",
    "tls-ticket-key-file",
    "rlimit-nofile",
    "backend-request-buffer",
    "backend-response-buffer",
    "no-server-push",
    "backend-http2-connections-per-worker",
    "fetch-ocsp-response-file",
    "ocsp-update-interval",
    "no-ocsp",
    "header-field-buffer",
    "max-header-fields",
    "include",
    "tls-ticket-cipher",
    "host-rewrite",
    "tls-session-cache-memcached",
    "tls-ticket-key-memcached",
    "tls-ticket-key-memcached-interval",
    "tls-ticket-key-memcached-max-retry",
    "tls-ticket-key-memcached-max-fail",
    "conf",
]

LOGVARS = [
    "remote_addr",
    "time_local",
    "time_iso8601",
    "request",
    "status",
    "body_bytes_sent",
    "remote_port",
    "server_port",
    "request_time",
    "pid",
    "alpn",
    "ssl_cipher",
    "ssl_protocol",
    "ssl_session_id",
    "ssl_session_reused",
]

if __name__ == '__main__':
    gentokenlookup(OPTIONS, 'SHRPX_OPTID', value_type='char', comp_fun='util::strieq_l')
    gentokenlookup(LOGVARS, 'SHRPX_LOGF', value_type='char', comp_fun='util::strieq_l', return_type='LogFragmentType', fail_value='SHRPX_LOGF_NONE')
