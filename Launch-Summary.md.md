
# WVU launches

### launch 1: March 01

- Systems onboard: APRS + WSPR (with a NEO6M GPS)
- The GPS on the WSPR module only rated for 10 km this was a low cost test of the WSPR payload for recoverability
- APRS worked well but WSPR packets were not sent out
- Recovery team heard partial packets in and around the predicted location unable to decode
- Conclusions:
	- APRS was resetting the WSPR GPS every 2 minutes and that prevented lock on the WSPR GPS causing it to not send out any data
	- Try to implement GPS sync on the APRS packets and a software bug was found after launch which explains unreadable packets

![](bin/Pasted%20image%2020250409183253.png){: width="600" }

## Launch 2: March 18 (during spring break)

- WSPR was the only payload with a PD1616 GPS (this is the same GPS that worked well)
- WSPR worked well but lot tracking
	- No altitude information or power information
	- We suspected a power drop might cause the system to fail 
![](bin/Pasted%20image%2020250409183953.png){: width="300" }

## Launch 3: April 04
- original launch date on 03/28 was cancelled 
- WSPR only payload with designed PCB
- 36 inch parachute to avoid high speed decent 
- Altitude encoding capability added
- Data and more details here: [2025-04-04](docs/WSPR/2025-04-04.md)
	- GPS lock failure was evident looking at the packets it sent.
	- A better GPS like the [Ublox M10Q](https://www.digikey.com/en/products/detail/u-blox/MAX-M10S-00B/15712909?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Medium%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20223376311_adg-_ad-__dev-c_ext-_prd-15712909_sig-CjwKCAjwtdi_BhACEiwA97y8BJtffdt_9E13R_ZxoFa6HcO6GMHjJrhPrsNDatPEv9z4wMNWhE3GOBoCGgAQAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlg1KX8lz4fZktf82JHCpDvZ8&gclid=CjwKCAjwtdi_BhACEiwA97y8BJtffdt_9E13R_ZxoFa6HcO6GMHjJrhPrsNDatPEv9z4wMNWhE3GOBoCGgAQAvD_BwE) this requires a redesign of the schematic
	- Putting a battery backup for hot restarts is an option

## Launch 4: Pending

- Possible APRS testing with newly fixed code