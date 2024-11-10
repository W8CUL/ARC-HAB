# Testing WSPR RX

-  Used a (tr)uSDX to receive WSPR on 20 m using the shack Yagi
	- internal sound card was not working on Shack PC
		- used an external USB sound card to configure WSJT-x
		- Uploaded the results to WSPR net.
		- This is a functional system to test our designs internally

![bg left width:600](bin/Pasted%20image%2020241109154119.png)


---
## 09/11/2024 - Discussion

Following discussion: 
- tasks added to issue log
- potential items to buy/make
	- audio cable for (tr)usdx 
	- Windows tablet to run WSJT-x? 
	- test board to run WSJT-x and clock chip 

![bg right width:400](https://github.com/user-attachments/assets/cf89e6af-d616-42bd-a424-bd9e920445b9)

---
## Rx using Kiwi web SDR - 10/11/2024

- Kiwi doesn't support online WSPR decoding
- Make sure the frequency is exactly `14095.600`
- Tested WSJT-X on Ubunutu. Gave good results 
	- Settings screen on Ubunutu

![300](bin/Pasted%20image%2020241110102918.png)
### Possible questions
- Is there a max time limit for public SDRs
- In windows can the redirection be done easily

---
