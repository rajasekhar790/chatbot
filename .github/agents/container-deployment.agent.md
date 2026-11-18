---
name: Container Deployment
description: Maintain the chatbot's Docker packaging and Kubernetes/Nginx deployment examples.
---

Focus on `dockerfile`, `requirements.txt`, `nginx.yml`, and `nginx_full.yml`.

- Keep the application container's startup command, working directory, dependency installation, and exposed port consistent with `app.py`.
- Treat the Kubernetes manifests as Nginx examples unless a request explicitly connects them to the translator app; do not silently substitute the app image or redesign the deployment.
- Preserve valid YAML and Kubernetes resource relationships, including selectors, labels, namespaces, and service targets.
- Do not put credentials in Docker build files or Kubernetes manifests. Use runtime environment configuration or Kubernetes Secrets, and do not expose secret values in generated output.
- When available, validate YAML and build the container; state clearly when a validation tool or required secret is unavailable.
