# Back-end-Development-Capstone

## Run locally

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```

Open `http://127.0.0.1:8000/`, `http://127.0.0.1:8000/songs/`, and
`http://127.0.0.1:8000/photos/`. On the Songs page click **Lyrics** and
capture the Bootstrap modal for `django-song-modal.jpg`. Capture the terminal
after `migrate` for `django-migrate.jpg`, the home page for
`django-app-browser.jpg`, and the gallery for `django-photos.jpg`.

## Docker Compose and deployment

From the parent directory run `docker compose up --build`. The three services
are available on ports 3000, 3030, and 8000. The commands in `run_all.sh`
produce the API and page checks used for deployment screenshots. For
Kubernetes, build/tag the images as `pictures:latest`, `songs:latest`, and
`django-capstone:latest`, then run:

```bash
kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
kubectl get pods,services
```

These commands cover the deployment checks (`deploy-getpic-*`,
`deploy-getsong-*`, `deploy-getdjango-*`) and provide a reproducible status
screen for the 30 rubric tasks.
