# Phase 5: Deploy

**Goal:** Run the service the way Acme's IT team will: containerized, configured by environment, observable.

## Tasks
1. Build and run the container:
   ```bash
   docker build -t acme-api .
   docker run --rm -p 8000:8000 --env-file .env acme-api
   curl localhost:8000/health
   ```
2. Move config (data path, model name) into environment variables with sensible defaults.
3. Add structured logging: one log line per request with path, status and duration.
4. Write down how this would run in Acme's AWS account (e.g. ECS or App Runner; secret in Secrets Manager).
   You don't need to deploy to AWS; the point is to answer Lee's questions.

## Concepts to learn
- 12-factor config: code is the same everywhere, environment differs.
- Secrets management: never in the image, never in git.
- Health checks and logs are what the on-call person sees at 2 a.m.

## Done when
- [ ] `docker run` works and `/health` returns ok.
- [ ] A short "deployment plan" section exists in the decision log, reviewed against Lee's concerns.
