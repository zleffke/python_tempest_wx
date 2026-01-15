# python_tempest_wx
Repository for working with Tempest Weather Station data

## Notes
This project is working with a Tempest ST which DOES NOT send the `air_obs` or `sky_obs` message type.  
It DOES send the `rapid_wind` message every three seconds (confirm time).  
It DOES send the Tempest Observation `obs_st` type every minute.  
It DOES Send the `hub_status` message periodically (check time).
I think I even saw a `device_status` message in there somewhere.

## References
### [Tempest UDP Broadcast API](https://apidocs.tempestwx.com/reference/tempest-udp-broadcast)
Useful for decoding the varios JSON message formats.

