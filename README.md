# Senior ML Engineer Tech Assessment
Private repository for my suggested solution to Loka's test

## Scenario
Company X has a large amount of documentation that their developers need to navigate. They have
noticed that their developers often spend significant amounts of time searching through documentation
or asking other developers simple questions that are in the documentation. The Company has reached
out to Loka's candidate to assist with building a tool to address this issue.
After some discussion, it is agreed that the first step of the collaboration should be a POC whose
goal would be to prove that the system would significantly shorten the amount of time developers spend
looking through documentation. The POC will cover only a subset of their data and will initially just be
applied to one of the teams.  
Upon further investigation, they mention that their main goal would be to have a system that could
assist developers with parts of the documentation they aren’t familiar with, as in these cases they typically
reach out to coworkers with some pretty simple questions. This has several issues, among them experienced
members have their work interrupted often and responses are sometimes based on old information, as
documentation is often updated, causing problems down the line. They would also like for the system to
be able to point the user to further reading, by pointing them towards the source for the response and
towards other documents that may be relevant to what they are currently working on. However, this last
request is a nice-to-have and not a mandatory feature. They can accept this being implemented later.
The documentation provided for the POC is public (it’s AWS documentation) and as such has no limitations on usage.
However, the final system will also handle internal documentation that contains sensitive
information that has proprietary (can’t be shared or accessed externally) and geographical restrictions
(can’t leave the US).  
They also provided some example questions they would like the system to be able to respond to for
the POC:  
• What is SageMaker?  
• What are all AWS regions where SageMaker is available?  
• How to check if an endpoint is KMS encrypted?  
• What are SageMaker's Geospatial capabilities?  

My task is to design the overall solution for Company X. Determine what parts of that solution
should be part of the POC and begin implementing the POC.  

## Proposed solution Introduction
Since Loka's team has a preference for AWS services, the proposed solution will primarily consider 
using AWS services.   

One of the central AWS services considered in the proposed solution will be Amazon Kendra; Amazon Kendra is 
an Intelligent search service powered by machine learning, it goes beyond the traditional key-word search method
by adding an extra layer of ML models to incorporate contextual and semantic understanding.  

These are some of the benefits of using this service for the proposed solution:  
* Amazon Kendra is easy to learn and use.
* By using AWS crawlers you can directly retrieve the context information from the source, in this case,
  the [AWS SageMaker documentation web page](https://docs.aws.amazon.com/sagemaker/),
  this is way better than manually getting the updated .md files every time there is a change on the documentation.
* Amazon Kendra uses machine learning to improve search results on your indexed data.
* Amazon Kendra is as secure as any other AWS cloud service, so you should not worry too much about
  using your enterprise data or documentation as input for this service.


  
