## Testing WSPR RX with (tr)USDx

-  Used a (tr)uSDX to receive WSPR on 20 m using the shack Yagi
	- internal sound card was not working on Shack PC
		- used an external USB sound card to configure WSJT-x
		- Uploaded the results to WSPR net.
		- This is a functional system to test our designs internally

![bg left width:600](bin/Pasted%20image%2020241109154119.png)


---
## Discussion
09/11/2024 by KC3VOP,KE8TJE

Following discussion: 
- tasks added to issue log
- potential items to buy/make
	- audio cable for (tr)usdx 
	- Windows tablet to run WSJT-x? 
	- test board to run WSJT-x and clock chip 

![bg right width:400](https://github.com/user-attachments/assets/cf89e6af-d616-42bd-a424-bd9e920445b9)

---
## WSPR Kiwi web SDR
10/11/2024 by KE8TJE

- Kiwi doesn't support online WSPR decoding
- Make sure the frequency is exactly `14095.600`
- Tested WSJT-X on Ubunutu. Gave good results 
	- Settings screen on Ubunutu

![300](bin/Pasted%20image%2020241110102918.png)
### Possible questions
- Is there a max time limit for public SDRs
- In windows can the redirection be done easily

---


### System testing 

1/16/2025 by KC3VOP, KE8TJE
tested tx with arduino and ft8 and rx signals with wsjtx and trusdx 
![image](https://github.com/user-attachments/assets/9e9c2395-4624-4d43-ae75-07bfba8623e2)
we were able to recive signals but not decode troubleshooting them now.
we possibly need to set auduino to sync time with global time as time syncing on both ends is very important for ft8
time was shown to be exact on Dylans windows laptop and hasiths linux laptop, unable to check time on arduino 

