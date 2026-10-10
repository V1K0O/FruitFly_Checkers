
library(plumber)

# Load the API routes from plumber.R
api <- plumber::pr("plumber.R")

# Start the API
api$run(
  host = "127.0.0.1",
  port = 8000,
  swagger = TRUE
)
