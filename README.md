This is an OAuth REST API project.

DJANGO REST Framework Views: 1. API View    2.ViewSet

1. API View:
    Is a basic to build our API , it enables us to describe the logic which makes our API endpoint.
    API View allows us to define functions that match the standard HTTP methods :
    HTTP GET: to get one or more items
    HTTP POST: to create an item
    HTTP PUT: to update a whole item
    HTTP PATCH: to update a particular field of an item
    HTTP DELETE: to delete an item

    Gives us the most control over the logic:
        - perfect for implementing complex logic
        - Calling other API's
        - Working with local files.
Serialization:
    Serializer is a feature in django that easily convert data inputs into python objects and vice versa.
    