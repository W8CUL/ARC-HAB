# WSPR - Payload
## Table of content 

- [Introduction](##Introduction)
- [WSPR Receive](WSPR_RX.md)
	- [WSPR with a radio](./WSPR_RX.md#testing-wspr-rx-with-trusdx)
	- [WSPR with public SDR](./WSPR_RX.md#wspr-kiwi-web-sdr)
- [DIY WSPR](./2024-12-17.md) 
## Introduction

Weak Signal Propagation Reporter (WSPR) is a data mode that has become very popular in evaluating the propagating and band conditions using a distributed network of global stations and the power of the internet to collect,store and visualize the data.

The main goal of this sub project is to evaluate the feasibility to use WSPR as a method of tracking the final landing location of the balloon. Following are some of the design goals we are actively trying to achieve 

- Light weight and low cost stand alone WSPR beacon
- Evaluate methods of sending 8 digit grid locations based on standard WSPR
- Encode altitude in to the power fields
