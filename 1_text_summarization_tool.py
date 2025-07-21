from transformers import pipeline       

#created the summarizer pipeline
summarizer = pipeline("summarization")  

#paragraph can be replaced file or user input
paragraph = """Internships play a crucial role in a student's academic and professional journey. 
They provide real-world experience by allowing students to apply theoretical knowledge in practical settings. 
Through internships, students gain industry exposure, improve their technical and soft skills, and develop a deeper understanding of workplace dynamics. 
Internships also help build confidence, foster professional networking, and often open doors to full-time job opportunities. 
By working on real projects and interacting with experienced professionals, students become more career-ready and aware of their interests and strengths."""


#it will generate the summary
summary = summarizer(paragraph, max_length=60, min_length=25, do_sample=False)

#it prints the original text
print("Original Text:\n", paragraph)

#it prints the summary of the text
print("\nSummary:\n", summary[0]["summary_text"]) 