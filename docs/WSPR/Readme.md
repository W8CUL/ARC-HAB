# WSPR - Payload
## Table of content 

- [WSPR Receive](WSPR_RX.md)
	- [WSPR with a radio](./WSPR_RX.md#testing-wspr-rx-with-trusdx)
	- [WSPR with public SDR](./WSPR_RX.md#wspr-kiwi-web-sdr)
- [DIY WSPR](./2024-12-17.md)
	- Signal generation testing
	- Decoding testing 
	- [Final code and PCB](https://github.com/W8CUL/WSPR_main) -  External git hub link
## Introduction

Weak Signal Propagation Reporter (WSPR) is a data mode that has become very popular in evaluating the propagating and band conditions using a distributed network of global stations and the power of the internet to collect,store and visualize the data.

The main goal of this sub project is to evaluate the feasibility to use WSPR as a method of tracking the final landing location of the balloon. Following are some of the design goals we are actively trying to achieve 

- Light weight and low cost stand alone WSPR beacon
- Evaluate methods of sending 8 digit grid locations based on standard WSPR
- Encode altitude in to the power fields ?

## Final design

A PCB was designed after all the testing and it was tested in two balloon flight. Key findings are below:
- WSPR packet generation was successful 
- Altitude can be encoded to the power field for debugging 
- GPS Issues:
	- During 2 separate launches we tested a NEO6M vs a PD1616 GPS
	- GPS lock was not consistent after 10 km, this caused WSPR to stop providing locations
## Data analysis

- 2025-04-04 flight data and more information [here](2025-04-04.md)

## Todo list

- Si5351 library for signal generation ✅ 2025-01-16
- FT8/WSPR packet generation ✅ 2025-01-16
- [Correct packet decoding ✅ 2025-01-16](2025-01-16.md)
- GPS Time syncing ✅ 2025-02-23
	- [x] GPS location to grid ✅ 2025-04-04
	- [x] 8 char grid Tx using 2 time slots ✅ 2025-04-04
- Full System testing ✅ 2025-02-23
	- [x] Battery powered system testing ✅ 2025-04-04
