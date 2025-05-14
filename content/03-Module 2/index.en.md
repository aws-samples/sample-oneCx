---
title : "Module 2 - Product offer recommendations and negotiation using agentic workflows"
weight : 30
---

# Introduction

Customer retention offers and cross-sell upsell offers are capabilities that help retain customers and grow their lifetime value respectively. Currently these capabilities are powered by heuristic algorithms or black box ML models, which reduce the ability for communications service providers to differentiate themselves in the market. Generative AI and agentic workflows provide a novel approach that allows business strategists within  CSP to have more control around using the power of AI in a no-code low-code environment. Not just that, making these offers available to customers through a self-service bot powered by GenAI, provide a personalized experience for customer the customer upgrade journey whilst cutting down on operational costs for the communications service provider. In this module, you will build an agentic workflow to provide product recommendations powered by the prompt flows feature in Agents for Amazon Bedrock. You will also see how we can use these offer recommendations along with their negotiation bands in generative AI chatbot to power zero-touch offer negotiations.

We will go through some of the components of the prompt flow, which have been pre-deployed for you (prompts, lambda functions, and agents) to examine how the underlying solution has been built. Then, we will use these components to build the prompt flow via the AWS console. Finally, we will test the end to end product recommendation flow by generating an event on a customers' journey that qualifies the customer for an offer.

The below image shows the functional flow that you will build:

:image[Functional Architecture]{src="/static/Module3/images/functional-architecturev1.png" width = 500 height = 400 style="float: left; margin-right: 10px;" disableZoom="true"}


# Module steps

Please work through the following steps in sequence. The steps are a mix of build and review of pre-built resources (this is in interest of the time we have at hand). Most steps are accompanied by screen-shots to provide you some visual guidance in addition to the textual description.
