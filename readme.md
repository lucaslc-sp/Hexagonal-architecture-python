# Python - Hexagonal Archictecture

This project has the aims to propose an architecture for decoupled projects made in python.

UNDERSTAND ALL OF THIS, BUT USE ONLY WHAT YOU NEED.

## Why for decoupled projects ?

When I use the term "for decoupled projects" this doesn't mean that we need to do a complex architecture.  In a company, an architecture decision has always so many variables involved from time, possibility of changes, languages to frameworks and people's knowledge.

So, my goal with this proposal is resolve a complex problem with the most simple and logical architecture. ```Always preserving the possibility of exchanging any part of the project and the maintenance```

## Architecture

The project is based on hexagonal architecture, which aims to divide the application into layers accordging to your responsibilities and emphasize the domain layer.



### Pre-Requisites

- Python 3.6+
- React
- Docker

### Why backend and frontend in the same project ?

It's was a difficult decision for me. There's a tradeoff decision for use backend and frontend in the same project:

Pros:

Con:

## Use Case

The context for this project is generate demmand for the supply chain.

Supply chain
    - Demand recorder

## Starting Project




## References

- https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together

- https://medium.com/raa-labs/part-1-domain-driven-design-like-a-pro-f9e78d081f10

- https://github.com/ajgrover/hexagonal-architecture-python

- https://github.com/Ermlab/python-ddd

- https://tuhrig.de/messages-vs-events-vs-commands/

- https://barryvanveen.nl/blog/59-different-kinds-of-service-bus-command-bus-service-bus-and-query-bus

- https://blog.lingoapp.com/implementing-a-command-bus-in-python-18b60bbe216