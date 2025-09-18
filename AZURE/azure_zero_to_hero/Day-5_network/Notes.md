# Day -5

- Understanding Network Security
- virtual Networks (VNets)
- Azure Networking Services
- Implementing Virtual Networks
- Network Security Groups (NSGs)
- Azure Firewall Overview

-- 
## Virtual Networks (VNets) why ? in AWS we called as VPC
    - Devops engineer at nike is creating the vm in us-east region with zone 1
    - Devops engineer at puma is creating the vm in us-east region with zone 1
    - Both the request are go through ther resource manager and processes
    - request goes to particular data center in us-east region
    - in the data center there are multiple racks
    - suppose nike request goes to rack x and puma request goes to rack x

    - VNET
        - VNET is a logical isolation of the azure cloud dedicated to your subscription
        - puma and nike both are using the same rack but they are not able to communicate with each other
        - puma has separate vnet and nike has separate vnet
    - Size can be mesured in terms of number of ip addresses / CIDR notation 
        - /16 - 65536 ips
    - NSG
        - Network security group is a set of rules that allow or deny network traffic to resources connected to Azure Virtual Networks (VNets).
        - for a particular subnet we can create a nsg and attach it to subnet
        - for easy understanding 
            - nsg is like a firewall
            - subnet is like a room
            - vnet is like a house
            - resource group is like a building
            - azure region is like a city
            - azure subscription is like a country

            - there are two subnets in a vnet
                - subnet 1 - web servers, app servers
                - subnet 2 - db servers
             - logic for the subnet can be accessed by internet 
             and subnet 2 can be accessed by subnet 1 like app servers can access db servers
                - subnet 2 should not be accessed by internet directly
              - cidr block ranges can connect to subnet 2 
              - anybody from internet should not be able to access subnet 2
              - this is the job of nsg
        - in REAL WORLD we use nsg+ASG (Application Security Group)
        - for suppose the subnet 1 has cidr range of 10.0.3.0/24
        - in NSG, anything coming from the source 10.0.3.0/24 can access subnet 2
        - in the destination we can provide all the databases

        - with ASG
            - if we have 5 web servers and 5 app servers
            - only app servers should connect to db servers
            - all the app servers should be grouped in on ASG

        - Route tables and user defined routes
            - how should the traffic flow between the subnets
            - by default all the subnets in a vnet can communicate with each other
            - if we want to restrict the communication between subnets we can use route tables and user defined routes
            - for suppose we have 3 subnets in a vnet
                - subnet 1 - web servers
                - subnet 2 - app servers
                - subnet 3 - db servers
            - we want to restrict the communication between subnet 1 and subnet 3
            - we can create a route table and add a user defined route to it
            - in the user defined route we can specify the destination as subnet 3 and next hop as virtual appliance (firewall)
            - this way all the traffic from subnet 1 to subnet 3 will go through the firewall    
------------------------------------------------------------------------------------------------------------------
## in a real world scenario
    Got it 🚀 Let’s make your **Azure VNets, NSGs, and Firewalls** lesson into a **movie scene** so it sticks in your head like a story you won’t forget.

---

🎬 **Title: The Great Cloud City**

🌆 *Scene 1 – The Big City*

* Imagine **Azure Region** as a **huge futuristic city**.
* Inside this city, there are **multiple buildings** → each building is a **Resource Group**.
* Inside each building, there are **apartments (houses)** → each house is a **VNet**.

🏠 *VNet* = Your **house**, logically isolated.

* Nike lives in one house.
* Puma lives in another house.
* Even if both houses are in the **same building and even on the same floor (rack)**, their walls are soundproof → **they can’t talk to each other unless you allow it**.

---

🌇 **Scene 2 – The Rooms Inside the House**

* Inside Nike’s house (VNet), there are **rooms (subnets)**:

  * Living room → **Web/App servers**
  * Bedroom → **Database servers**

But… the **bedroom is private**. No one from the street (Internet) can walk in directly.
Only people from the living room (App servers) are allowed to enter the bedroom.

---

🛡️ **Scene 3 – The Bodyguards (NSGs)**

* At the door of each room, Nike hires **NSG bodyguards**.
* These guards have **rules written on a clipboard**:

  * *“If you are from the Internet, you can only come into the living room.”*
  * *“If you are from the living room, you may enter the bedroom (DB).”*
  * *“No one from the street can go directly into the bedroom.”*

That’s the job of the **NSG** – like a **firewall at every door**.

---

👥 **Scene 4 – The VIP Guest List (ASG)**

* Now Nike throws a party and has 5 guests in the living room (Web servers) and 5 in the kitchen (App servers).
* Only the **App server guests** should talk to the **Database room**.
* Instead of writing rules for every single guest, Nike says:

  * *“All App server guests wear a badge = ASG.”*
  * Guard checks the badge → only those with the **App badge** can enter DB room.

---

🛣️ **Scene 5 – Roads and Highways (Route Tables + UDRs)**

* By default, all rooms (subnets) in the house are connected with hallways → free movement.
* But what if Nike wants to block movement between the Living room (Web servers) and the Bedroom (DB servers)?

Solution:

* Nike rebuilds the hallway with a **detour road**.
* He places a **checkpoint (firewall/virtual appliance)** in the middle.
* Now, if Living room wants to talk to Bedroom, they must **pass through the firewall checkpoint**.

---

🔥 **Scene 6 – Azure Firewall**

* Think of Azure Firewall as the **giant security gate at the entrance of the entire house**.
* It filters everything before anyone even gets close to the rooms.

---

🎬 **Final Takeaway (One-Line Memory Hooks):**

* **Azure Subscription** = Country 🌍
* **Region** = City 🏙️
* **Resource Group** = Building 🏢
* **VNet** = House 🏠
* **Subnet** = Room 🚪
* **NSG** = Bodyguard with rulebook 🛡️
* **ASG** = Guest list badge 🎟️
* **Route Table + UDR** = Custom hallways/roads 🛣️
* **Firewall** = Main security gate 🔥

---

👉 Every time you think of VNets, picture this **movie in your head**: Nike and Puma living in the same futuristic city, but with separate, guarded, badge-controlled houses.

Do you want me to make this into a **comic-style diagram/storyboard** too? That’ll lock it into your memory even harder.
-----------------------------------------------------------------------------------------------------------------------