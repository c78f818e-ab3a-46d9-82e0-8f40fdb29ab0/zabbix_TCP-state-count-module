



# This will create the tcp_state.so file. Put it into a /usr/lib/zabbix/modules directory for example.
mkdir -p /usr/lib/zabbix/modules



# Configure
#---------------------------------------------------------------------
# For an agent : /etc/zabbix/zabbix_agentd.conf
# For a server : /etc/zabbix/zabbix_server.conf
# For a proxy : /etc/zabbix/zabbix_proxy.conf

LoadModulePath=/usr/lib/zabbix/modules
LoadModule=tcp_state.so

# By default, the packages will create a /etc/zabbix/zabbix_agentd.d/modules.conf file with parameters above.





# restart zabbix-agent service
systemctl restart zabbix-agent.service



# You can test it like this for example if you configured a Zabbix agent to load the module:
zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf -t net.tcp.count[10051]




