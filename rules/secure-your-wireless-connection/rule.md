---
type: rule
title: Wireless - Do you secure wireless connections?
seoDescription: Secure your wireless connection and prevent unauthorized access to your office network with WPA3-Enterprise authentication using Radius servers and Active Directory.
uri: secure-your-wireless-connection
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
related:
  - easy-wifi-access
redirects:
  - do-you-secure-your-wireless-connection
created: 2017-07-10T21:37:12.000Z
archivedreason: null
guid: be6d9987-405c-44a3-b204-913dd7ce3f56

---

Wi-Fi is everywhere now. You can't drive down the street without finding a network which is insecure. However, in an office environment, there is a lot more to lose than a bit of bandwidth. It is vital that wireless is kept secure.

Office Wi-Fi should use WPA3-Enterprise, using RADIUS to securely authenticate users.

<!--endintro-->

::: bad
![Figure: Bad example - Unsecured network (OK for guest networks with a Captive Portal)](wifi-unsecured.jpg)
:::

::: good
![Figure: Good example - WPA3 Enterprise](ios-wpa3-ent.png)
:::

Some things to note:

* WPA3 has been around for a while, but some devices still have compatibility issues. testing should be done before moving from WPA2 to WPA3
* You should have a separate, isolated guest network, as per: [Wireless - Do you provide guests with easy Wi-Fi access?](/easy-wifi-access)
* You may need other SSIDs as well, for example an IoT network. IoT devices may only be compatible with WPA2 Personal; these networks should be isolated and locked down as appropriate

## Setting up enterprise Wi-Fi

Here's an example of how office Wi-Fi can be set up. Note that various authentication methods can be used, such as username/password, smart cards, or certificates.

### Requirements

* 802.1X-capable 802.11 wireless access points (APs)
* Active Directory with Group Policy
* Network Policy Server (NPS)
* Active Directory Certificate Services, or a third-party certificate

1. **Configure Wireless APs**

  * These steps will vary between vendors
  * You'll need to enter:
  
    * NPS server IP address
    * Port (default is 1812)
    * A shared secret - create a secure password

  ![Figure: UniFi RADIUS settings](unifi-radius.png)

2. **Install NPS on your server**

   On Windows Server, open server manager and add the **Network Policy and Access Services** role. Under role services add:

   * Network Policy Server
   * Routing and Remote Access Services

3. **Configure Radius Clients on NPS**

   * Open up the NPS Console
   * Right click on **Radius Clients | New**
   * Fill out the fields for Friendly name (e.g. the AP name), IP address, and add the shared secret you configured on your access points

  ![Figure: Radius client settings](NPS2.png)

4. **Configure 802.1x on the NPS server**

   1. Click on NPS (Local)
   2. In the right-hand pane under standard configuration choose **Radius Server for 802.1x Wireless or Wired Connections**
   3. Click on **Configure 802.1X** to start a wizard-based configuration
   4. Select the top radio button **Secure Wireless Connections** click next
   5. On the Specify 802.1X Switches Page, check the APs you have configured under Radius Clients are in that list then click next
   6. Now the authentication method. From the drop-down lists select Protected EAP (PEAP)
      **NOTE:** This method requires a Computer Certificate and the Radius Server and either a computer or user certificate on the client machine
   7. Select the groups (e.g. Domain\WirelessAccess) you would like to give wireless access to. You can do this by user, computer, or both
   8. Configure VLANs if needed, or use the defaults
   9. Register the server with Active Directory - right-click on NPS (Local) and select Register Server in Active Directory

  ![Figure: How to register NPS server with AD](NPS.png)

  You should now have a Connection Request Policy and a Network Policy.

5. **Remove the MS-CHAP v1 authentication method** from the **Network Policy | Constraints** tab

6. **Configure Certificate Auto enrolment**

   1. Open Group Policy Management
   2. Create a new GPO policy and name it, e.g. "Cert_Enrollment_Wireless"
   3. Link it to the root of the domain, or a specific OU depending on your needs and OU structure
   4. Under the security filtering scope, remove **Authenticated Users** and add the Wi-Fi users group
   5. Click **Edit settings** and go to:
        1. Computer Configuration\Policies\Windows Settings\Security Settings\Public Key Policies  
           - In the Details pane, right-click the **Certificate Services Client – Auto-enrolment** and then select properties
           - Select enabled from the drop-down menu and check all tick boxes
        2. Computer Configuration\Policies\Windows Settings\Security Settings\Public Key Policies\Automatic Certificate Request Settings
           - Right-click in the details pane and select **New | Automatic Certificate Request**
           - This will open up a wizard and you can select a Computer Certificate

      ![Figure: Group policy settings](Cert4.png)
      
7. **Creating a Windows Wireless 802.1x GPO Policy**

   1. Now go to Computer Configuration\Policies\Windows Settings\Security Settings\Wireless Network (IEEE 802.11) Policies
     * Right-click | **Create a new policy**

   2. Enter a Policy Name (e.g. WiFi_Settings) and description and link to the root of the domain
      ![Figure: GP link and scope settings](Cert3.png)

   3. Click **Add**, enter a Profile Name and add the SSID from the Wireless APs
     * Make sure the tick box **Connect Automatically when this network is in range** is ticked

   4. Click on the Security Tab
     * Make sure Authentication is **WPA3-Enterprise** and Encryption is **AES**
     * Under "Select a network authentication method, choose **Microsoft: Protected EAP (PEAP)**
     * Under Authentication Mode, you need to choose whether you want to authenticate computers and/or users with digital certificates
     * Select **Computer Authentication**

   5. Click on **Properties**
     * Tick **Validate server certificate**, tick **Connect to these servers**, and enter the FQDN of the NPS server
     * Under **Trusted Root Certification Authority**, tick your Root CA certificate
     * Click OK
       ![Figure: Connection security settings](Cert2.png)
     
       **Optional:** Under Network Permission tab you can use the tick boxes to restrict clients to infrastructure networks or only GPO profiled allowed networks if you desire.

   6. You have completed your Enterprise Wireless Policy
      ![Figure: Wi-Fi_Settings settings](GPU.png)
