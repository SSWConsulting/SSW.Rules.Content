

---
authors:
  - id: 55
    title: Steve Leigh
---




<span class='intro'> <p>Each file in TypeScript is a module, and each module can export whatever members it wants.&#160; However, if you export everything, you run the risk of having to increment major versions (when using semantic versioning), or having your module used in unintended ways. </p> </span>

<p>​​Only export the types necessary to reduce your API surface.&#160; Often, this means exporting interfaces over implementations.</p>


