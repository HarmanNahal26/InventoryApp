# Inventory App

This project is a cloud-based inventory management system built using AWS services. It allows users to perform basic operations such as retrieving all inventory items, viewing a specific item, adding new items, deleting items, and retrieving items based on location.

The application uses DynamoDB to store inventory data, AWS Lambda to handle backend logic, and API Gateway to expose RESTful endpoints. A simple static website is hosted on Amazon S3 to demonstrate web hosting functionality.

GitHub Actions is used to implement CI/CD automation. The Super Linter runs when pull requests are opened, and deployments occur automatically when changes are merged into the main branch. Lambda functions are updated when code changes are made, and the S3 website is updated when the index.html file is modified.

It is important to note that all Lambda functions are created manually in AWS before deployment, as GitHub Actions only updates existing functions and does not create new ones.

This project demonstrates the integration of cloud services, automation workflows, and API development in a complete working system.


