# **App Name**: ContextFlow

## Core Features:

- Users Context: Defines the Users context, encapsulating user-related domain logic, application services, and infrastructure adapters.
- Auth Context: Defines the Auth context, handling authentication and authorization concerns with its own domain, application, and infrastructure layers.
- Create User Command: Implements commands via RabbitMQ to create users, ensuring asynchronous processing and scalability.
