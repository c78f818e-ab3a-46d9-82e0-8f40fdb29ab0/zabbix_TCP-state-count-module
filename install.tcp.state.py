



# This will create the tcp_state.so file. Put it into a /usr/lib/zabbix/modules directory for example.
mkdir -p /usr/lib/zabbix/modules



# Configure
#---------------------------------------------------------------------
# For an agent : /etc/zabbix/zabbix_agentd.conf
# For a server : /etc/zabbix/zabbix_server.conf
# For a proxy : /etc/zabbix/zabbix_proxy.conf

LoadModulePath=/usr/lib/zabbix/modules
LoadModule=tcp_state.so





