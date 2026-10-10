
#* Check whether the R server is running
#* @get /health
function() {
  list(
    status = "OK",
    service = "Checkers FlyBrain",
    r_version = R.version.string
  )
}

#* Check whether required packages are installed
#* @get /status
function() {
  list(
    status = "OK",
    plumber_version = as.character(packageVersion("plumber")),
    malecns_installed = requireNamespace("malecns", quietly = TRUE)
  )
}


#* Receive and validate a Checkers board
#* @post /test-board
#* @parser json
function(req, res) {
  body <- req$body
  
  if (is.null(body$board)) {
    res$status <- 400
    return(list(error = "Missing board field"))
  }
  
  board <- body$board
  
  # Handle either a matrix or a list of rows
  if (is.matrix(board) || is.array(board)) {
    dimensions <- dim(board)
    
    valid_board <- length(dimensions) == 2 &&
      dimensions[1] == 8 &&
      dimensions[2] == 8
  } else if (is.list(board)) {
    valid_board <- length(board) == 8 &&
      all(lengths(board) == 8)
  } else {
    valid_board <- FALSE
  }
  
  if (!valid_board) {
    res$status <- 400
    return(list(
      error = "Board must be an 8x8 grid",
      received_type = class(board),
      received_dimensions = dim(board)
    ))
  }
  
  list(
    status = "received",
    player = body$player,
    rows = 8,
    columns = 8,
    message = "Python board received successfully"
  )
}


#* Choose a legal move (temporary baseline)
#* @post /decide
#* @parser json
function(req, res) {
  body <- req$body
  
  if (is.null(body$board) || is.null(body$legal_moves)) {
    res$status <- 400
    return(list(error = "Board and legal_moves are required"))
  }
  
  moves <- body$legal_moves
  

  number_of_moves <- if (is.data.frame(moves)) {
    nrow(moves)
  } else {
    length(moves)
  }
  
  if (number_of_moves == 0) {
    res$status <- 400
    return(list(error = "No legal moves supplied"))
  }
  
  list(
    status = "ok",
    move_id = 0,
    message = "Temporary baseline: selected first legal move"
  )
}

