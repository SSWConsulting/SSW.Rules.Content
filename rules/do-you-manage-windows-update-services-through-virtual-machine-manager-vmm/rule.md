

---
authors:
  - id: 73
    title: Kaique Biancatti
---




<span class='intro'> <p>You can use Virtual Machine Manager (VMM) to manage your Windows Update Services (WSUS) directly, instead of using the server management itself.<br></p> </span>

<p>​To find full explained instructions on how to set this up, see <a href="https&#58;//docs.microsoft.com/en-us/system-center/vmm/update-server?view=sc-vmm-2019">here</a>.</p><p>Before&#160;starting, you should take&#160;some things into consideration&#58;</p><p>&#160; 1. The WSUS server must be in the same domain as the VMM server;<br>&#160; 2. Best practices dictates that you should use a separate server to be a WSUS server;<br>&#160; 3. After you add a WSUS server to VMM, you should use the VMM console to manage it, and not the WSUS console.</p><p>After taking these into consideration, you can start deploying update baselines, which contains a set of required updates scoped to objects, and adding update exemptions as necessary.<br></p>


