## Flask Application Design

### HTML Files

#### index.html:
- **Content:** Home page of the website with a search bar and a list of all Japanese restaurants.

#### search_results.html:
- **Content:** Results page that shows a filtered list of Japanese restaurants based on search criteria.

### Routes

#### Main Page Route:
- Defines the home page route, which renders the `index.html` file.
- URL: `/`

#### Search Results Route:
- Handles the search functionality and filters the list of Japanese restaurants based on user input.
- URL: `/search`

#### Route to Display a Specific Restaurant:
- Defines a route to display details of a specific Japanese restaurant.
- URL: `/restaurant/<restaurant_id>`