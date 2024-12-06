# Test the flask application (from cm-birds-main)
flask run
Application should be available at http://127.0.0.1:5000

# Build the docker image (from cm-birds-main)
docker build -t birds:latest .

# Test the docker image to make sure the image runs 
docker run -p  5000:5000 birds
Application should be available at http://127.0.0.1:5000

# Create the kind cluster
kind create cluster --name <kind-cluster-name>

# Load the image into kind
kind load docker-image birds:latest --name <kind-cluster-name>

# Deploy the docker image to kind (from cm-birds-main/helm/birds)
helm install birds . (or upgrade if already deployed)

# Get the pod name
kubectl get pods

# Get the service port to be forwarded - PORT(S)
kubectl get service birds

# forward the port for the pod
kubectl port-forward pod/[pod-name] [service-port]:5000
Application should be available at: http://127.0.0.1:[service-port]

# Note - the sqlite database seems to be a bit off.  Most of the states are fine, but from Maryland to Oregon the state names don't match the abbreviation - 
# Up to Maine and after Oregon (Pennsylvania is next) the names and abbreviations match
# Below is the output of the DB for these states.

{"state": "Maryland", "bird": "Baltimore oriole", "scientific_name": "Icterus galbula", "year": "1947", "abbreviation": "MT"}, 
{"state": "Massachusetts", "bird": "Black-capped chickadee", "scientific_name": "Poecile atricapilla", "year": "1941", "abbreviation": "NE"}, 
{"state": "Michigan", "bird": "American robin", "scientific_name": "Turdus migratorius", "year": "1931", "abbreviation": "NV"}, 
{"state": "Minnesota", "bird": "Common loon", "scientific_name": "Gavia immer", "year": "1961", "abbreviation": "NH"}, 
{"state": "Mississippi", "bird": "Northern mockingbird", "scientific_name": "Mimus polyglottos", "year": "1944", "abbreviation": "NJ"}, 
{"state": "Missouri", "bird": "Eastern bluebird", "scientific_name": "Sialia sialis", "year": "1927", "abbreviation": "NM"}, 
{"state": "Montana", "bird": "Western meadowlark", "scientific_name": "Sturnella neglecta", "year": "1941", "abbreviation": "NY"}, 
{"state": "Nebraska", "bird": "Western meadowlark", "scientific_name": "Sturnella neglecta", "year": "1929", "abbreviation": "NC"}, 
{"state": "Nevada", "bird": "Mountain bluebird", "scientific_name": "Sialia currucoides", "year": "1967", "abbreviation": "ND"}, 
{"state": "New Hampshire", "bird": "Purple finch", "scientific_name": "Carpodacus purpureus", "year": "1957", "abbreviation": "OH"}, 
{"state": "New Jersey", "bird": "Eastern goldfinch (American goldfinch)", "scientific_name": "Spinus tristis", "year": "1935", "abbreviation": "OK"}, 
{"state": "New Mexico", "bird": "Greater roadrunner", "scientific_name": "Geococcyx californianus", "year": "1949", "abbreviation": "OR"}, 
{"state": "New York", "bird": "Eastern bluebird", "scientific_name": "Sialia sialis", "year": "1970", "abbreviation": "MD"}, 
{"state": "North Carolina", "bird": "Northern cardinal", "scientific_name": "Cardinalis cardinalis", "year": "1943", "abbreviation": "MA"}, 
{"state": "North Dakota", "bird": "Western meadowlark", "scientific_name": "Sturnella neglecta", "year": "1970", "abbreviation": "MI"}, 
{"state": "Ohio", "bird": "Northern cardinal", "scientific_name": "Cardinalis cardinalis", "year": "1933", "abbreviation": "MN"}, 
{"state": "Oklahoma", "bird": "Scissor-tailed flycatcher", "scientific_name": "Tyrannus forficatus", "year": "1951", "abbreviation": "MS"}, 
{"state": "Oregon", "bird": "Western meadowlark\\n (state songbird)", "scientific_name": "Sturnella neglecta", "year": "1927\\n 2017", "abbreviation": "MO"}
