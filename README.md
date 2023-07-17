# Practical test for CHR company

In this repository you will find both resolute tasks and can prove them in a practical way.

<details><summary>Development Summary [es]</summary>
<p>

Como diferencial pensé en usar contenedores Docker usando Podman y en lugar de Bootstrap que ya conocía, decidí usar Tailwind que es una herramienta que he estado usando recientemente, pero que se ha convertido en mi Framework CSS favorito.

### Test 1

Fue realmente genial cómo indirectamente la prueba al principio te hace creer que hay una API documentada, pero al final del día la idea era entender la Network que pasaba dentro del sitio y a través de ella encontré el POST correcto y sus parámetros. Fue bastante divertido usar Requests lib en lugar de Django Rest. Requests es una herramienta que me resulta muy cómoda.

### Test 2

Usar Selenium 4 fue una buena experiencia, tuve experiencia con Selenium 3 y la forma de hacer todo fue mucho más agradable. Confieso que a pesar de esto, fue la tarea que más tiempo me costó, no por una limitación técnica, sino porque no me fijé desde el principio que toda la información importante y los selectores estaban en un HTML Frame aparte. Después de ese descubrimiento, todo fluyó.

</p>
</details>

## Requirements

- docker or podman
- docker-compose or podman-compose

## Setup

First you need to rename `.env.sample` file to `.env`.
For practical purposes. All information in .env.sample is already the necessary information for it to work. Of course, you have to double check Django's SECRET_KEY.

- Setup on Development

`docker-compose up --build`

- Setup on Production

`docker-compose -f docker-compose.prod.yml up --build`

## Test task resolution

- Task 1

`http://0.0.0.0:8000/jurisprudence/`

- Task 2

`http://0.0.0.0:8000/concessions/`
