CLEANED_GRAPH_DATA = {
    "nodes": [
        {
        "id": "node_5b734e8a",
        "name": "Inception",
        "type": "Movie"
        },
        {
        "id": "node_49d06efc",
        "name": "science fiction",
        "type": "Genre"
        },
        {
        "id": "node_81a80b08",
        "name": "2010",
        "type": "Release_Year"
        },
        {
        "id": "node_261e4dc0",
        "name": "Christopher Nolan",
        "type": "Person"
        },
        {
        "id": "node_f647fb83",
        "name": "Leonardo DiCaprio",
        "type": "Person"
        },
        {
        "id": "node_336e4206",
        "name": "Joseph Gordon-Levitt",
        "type": "Person"
        },
        {
        "id": "node_0c99da2e",
        "name": "Elliot Page",
        "type": "Person"
        },
        {
        "id": "node_314b5d80",
        "name": "Thriller",
        "type": "Genre"
        },
        {
        "id": "node_687320c5",
        "name": "Interstellar",
        "type": "Movie"
        },
        {
        "id": "node_74eabed3",
        "name": "Matthew McConaughey",
        "type": "Person"
        },
        {
        "id": "node_feb7448d",
        "name": "Anne Hathaway",
        "type": "Person"
        },
        {
        "id": "node_a03266f3",
        "name": "The Dark Knight Rises",
        "type": "Movie"
        }
    ],
    "edges": [
        {
        "source": "node_5b734e8a",
        "relation": "HAS_GENRE",
        "target": "node_49d06efc"
        },
        {
        "source": "node_5b734e8a",
        "relation": "HAS_RELEASE_YEAR",
        "target": "node_81a80b08"
        },
        {
        "source": "node_261e4dc0",
        "relation": "DIRECTED",
        "target": "node_5b734e8a"
        },
        {
        "source": "node_f647fb83",
        "relation": "STARS_IN",
        "target": "node_5b734e8a"
        },
        {
        "source": "node_336e4206",
        "relation": "STARS_IN",
        "target": "node_5b734e8a"
        },
        {
        "source": "node_0c99da2e",
        "relation": "STARS_IN",
        "target": "node_5b734e8a"
        },
        {
        "source": "node_5b734e8a",
        "relation": "HAS_GENRE",
        "target": "node_314b5d80"
        },
        {
        "source": "node_261e4dc0",
        "relation": "DIRECTED",
        "target": "node_687320c5"
        },
        {
        "source": "node_74eabed3",
        "relation": "STARS_IN",
        "target": "node_687320c5"
        },
        {
        "source": "node_feb7448d",
        "relation": "STARS_IN",
        "target": "node_687320c5"
        },
        {
        "source": "node_f647fb83",
        "relation": "ACTED_IN",
        "target": "node_a03266f3"
        },
        {
        "source": "node_261e4dc0",
        "relation": "DIRECTED",
        "target": "node_a03266f3"
        }
    ]
}   