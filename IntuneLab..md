# Microsoft Intune Lab: Lab Goal - Build a small Microsoft 365 and Intune environment from scratch to practice the core tasks of an endpoint support technician: creating users and groups, assigning licenses, enrolling a Windows device, applying compliance and configuration policies, deploying an app, and troubleshooting what goes wrong. I documented each step with screenshots, along with the problems I ran into and how I fixed them, so the work can be repeated and reviewed.
## TL;DR Home lab: Microsoft 365 and Intune administration (users, groups, licensing, device enrollment, compliance and configuration policies, app deployment, troubleshooting).
* **Created 3 test users; (Frontdesk Test was given Intune license as well, error in screenshots)**
  * Faculty desk, Frontdesk Test, Staff Test, and me, Charles, the Admin
  ![IntuneLab](screenshots/01-test-users.png)

* **step 2: identify verify-account endpoint**
  * capture and inspect the `post /WebGoat/auth-bypass/verify-account` request in zap history[cite: 3].
  ![zap endpoint detection](screenshots/02-zap-endpoint.png)

* **step 3: parameter manipulation in requester**
  * forward the verification request to zap requester to test tampering with the security question fields[cite: 3].
  ![zap requester tampering](screenshots/03-zap-tampering.png)

* **step 4: bypass verification**
  * delete `jsenabled` and modify `verifymethod` to successfully verify the account without valid answers[cite: 3].
  ![verification bypass success](screenshots/04-auth-bypass-success.png)

---
