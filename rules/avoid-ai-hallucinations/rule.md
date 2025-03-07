---
type: rule
tips: ""
title: Do you handle AI Hallucinations the right way?
seoDescription: "ai hallucinations how to avoid "
uri: avoid-ai-hallucinations
authors:
  - title: ""
guid: e4e963e4-1568-4e47-b184-d2e96bc0f124
---
AI is a powerful tool, however, sometimes it simply makes things up, aka hallucinates. While hallucinating in your spare time is pretty cool, it is very bad for business!
            
1. Place your intro here. This will show in the blurb.
            
<!--endintro-->

**Title: Do You Handle AI Hallucinations the Right Way?**  
**Abstract:** AI hallucinations are inevitable, but with the right techniques, you can minimize their occurrence and impact. Learn how SSW tackles this challenge using proven methods like clean data tagging, multi-step prompting, and validation workflows.  

---

### **The Problem: AI Hallucinations Are Unavoidable**  
AI models like GPT-4 are powerful but imperfect. They generate plausible-sounding but incorrect or nonsensical outputs—**hallucinations**—due to training limitations, ambiguous prompts, or flawed data retrieval. While you can’t eliminate hallucinations entirely, you *can* reduce their frequency and mitigate risks.  

---

#### **1. Use Clean, Tagged Data for RAG**  
**Bad Example:**  
*Untagged, messy data leads to garbage outputs.*  
```python  
# Bad: Untagged data in a RAG system  
documents = ["Sales grew 10% in 2023", "Server downtime: 5hrs in Q2"]  
# Query: "What was the server uptime in Q2?"  
# Hallucination: "Server uptime was 95%." (Wrong: No uptime data exists!)  
```
**Good Example:**  
*Tagged data ensures accurate retrieval.*  

```python  
# Good: Properly tagged data  
documents = [  
  {"text": "Sales grew 10% in 2023", "tags": ["finance", "sales"]},  
  {"text": "Server downtime: 5hrs in Q2", "tags": ["IT", "downtime"]}  
]  
# Query: "What was the server uptime in Q2?"  
# Output: "No uptime data found. Available data: 5hrs downtime." ✅  
```
**SSW Rule:** Always tag data with metadata (e.g., domain, date, source) to improve RAG accuracy.  

---

#### **2. Break Workflows into Multi-Step Prompts**  
**Bad Example:**  
*A single-step prompt invites hallucinations.*  

```  
User: "Write a blog about quantum computing benefits for SMEs."  
AI: Hallucinates fictional case studies and stats. ❌  
```
**Good Example:**  
*Multi-step validation reduces errors.*  

```  
Step 1: "Generate a blog draft about quantum computing for SMEs."  
Step 2: "Verify all claims in this draft against trusted sources."  
Step 3: "Compare the final draft to the original query. Did you answer the question?"  
```
**SSW Rule:** Use a **chain-of-thought** approach to split tasks into smaller, validated steps.  

---

#### **3. Force the AI to Justify Its Reasoning**  
**Bad Example:**  
*No justification = unchecked errors.*  

```  
User: "Why should SMEs adopt quantum computing?"  
AI: "It boosts efficiency by 200%." (Source? None!) ❌  
```
**Good Example:**  
*Require citations and self-reflection.*  
```  
System Prompt: "Answer the question and cite sources. If uncertain, say 'I don’t know'."  
User: "Why should SMEs adopt quantum computing?"  
AI: "Quantum computing can optimize logistics (Source: IBM, 2023). However, adoption costs may be prohibitive for SMEs." ✅  
```
**SSW Rule:** Always prompt the AI to **cite sources** and **flag uncertainty**.  

---

#### **4. Validate Outputs Against the Original Question**  
**Bad Example:**  
*No final check = off-topic answers.*  
```  
User: "How does Azure Kubernetes Service (AKS) simplify deployment?"  
AI: Explains Kubernetes basics (ignores AKS specifics). ❌  
```
**Good Example:**  
*Add a final validation step.*  

```  
System Prompt: "Compare your answer to the user’s question. Did you address AKS?"  
AI: "Revised answer: AKS simplifies deployment by integrating with Azure DevOps and..." ✅  
```
**SSW Rule:** Use a **validation layer** to ensure outputs align with the original query.  

---

### **Other Techniques to Minimize Hallucinations**  
- **Lower Temperature Settings**: Reduce creativity (e.g., `temperature=0.3`) for factual tasks.  
- **Human-in-the-Loop**: Flag low-confidence responses for manual review.  
- **Predefined Constraints**: Example: "Do not speculate beyond the provided data."  

---

### **How to Get It Wrong**  
- 🚫 **Ignoring Data Hygiene**: Untagged data in RAG guarantees flawed outputs.  
- 🚫 **Single-Prompt Workflows**: No checks = higher hallucination risk.  
- 🚫 **Overly Vague Prompts**: Example: "Write something about AI."  

---

### **Conclusion**  
AI hallucinations are unavoidable, but SSW’s proven techniques—clean data tagging, multi-step validation, and forcing justification—keep them in check. By designing workflows that **anticipate errors** and **validate outputs**, you turn a risky limitation into a manageable challenge.  

**Final Rule:** Always assume hallucinations *will* happen—build systems to catch them!  

---
**Tags:** AI Best Practices, RAG, SSW Rules, Prompt Engineering
