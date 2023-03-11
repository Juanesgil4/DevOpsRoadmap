# Continuous Integration / Continuos Deployement

<font size=1>
    Basado en el curso de <a href=https://www.youtube.com/watch?v=h9K1NnqwUvE&ab_channel=Simplilearn>
    SimpliLearn - CI/CD Full Course
    </a>
</font>

----


## Modelos de Despliegue

- **Cascada:** Es un modelo tradicional de desarrollo de software. Se capturan los requerimientos del cliente, se inicia a desarrollar, y posterior al desarrollo se entrega un producto al cliente. Las necesidades pudieron haber cambiado, los requerimientos y por tanto la entrega de valor.
- **Agile:** Como premisa pretende dar entregas de valor constantes e iterativas, obteniendo feedback y atendiendo las necesidades del desarrollo a medida que surgen. A partir de ceremonias, como daily, planning, refinement, sprints, reviews, retrospectives, se va a tener la oportunidad de mejorar iterativamente la entrega de valor, así como integrando el feedback y las necesidades del cliente. Sin embargo, el producto solo se testea en el computador del desarrollador y no en los sitemas productivos, y a veces, se puede trabajar en silos, y el equipo de operaciones es el encargado del despliegue. Si hay errores, se devuelve el código.

## DevOps
Es una evolución del modelo Agile, donde se integra que el equipo de Desarrollo (Dev) y el equipo de Operaciones (Ops). Por tanto, se agrupa en 8 fases que son: Plan, Code, Build, Test, Integrate, Deploy, Operate, Monitor.
- Plan: Etapa de planeación y organización de objetivos
- Code: Etaba de diseño donde se usan herramientas como Git para guardar el código en un repositorio
- Build: Herramientas para la infraestructura para el código
- Testing: Etapa donde se realizan pruebas unitarias, de integración, carga usando pytest o unittest
- Integrate: Jenkins como herramienta para llevarlo a las servidores
- Deploy: Para llevarlo a los servidores de producción
- Operate: Herramientas de operación y manejo de la implementación así como monitoreo.

### Continuous Integration
`Plan > Code > Build > Test` + `Continuous Integration` > `Release`
Es una práctica de desarrollo donde se integra el código dentro de un repositorio compartido. Cada integración es verificado por una automatización de build (infraestructura) y de pruebas. Planeamos los requerimientos, codificamos la propuesta de solución y construimos una infraestructura donde se pueda correr el código, la cual será testeada con un framework. Podemos identificar errores y defectos en el código. Si las pruebas son aprobadas, entonces podrá ser desplegado en entornos productivos.
- Desarrollar y Compilar
- Tests Unitarios
- Integración con Bases de Datos
- Despliegue en entornos pre-productivos
- Pruebas funcionales y etiquetado de código
- Reportería y análisis
Si se aprueban los desarrollos se integra a una rama superior, dependiendo de la metodología de desarrollo en GIT. Puede ser trabajar en ramas feature, hotfixes, o desarrollo, y luego integrar después de pasar pruebas.

### Continuous Deployment
El Despliegue Continuo es una extensión de la Integración Continua, donde se apunta a reducir el tiempo que un equipo de desarrollo se toma entre escribir una nueva línea de código y usarla en producción. No solo se tiene un feedback más rápido por el cliente, sino un retorno de la inversión mucho más pronto. De esta manera, se va a reducir la interacción humana, brindando mayor precisión.
- Desarrollo
- Almacenamiento
- QA
- Teste
- Producción

### Ventajas
- Se reduce el tiempo para crear y desplegar software
- Se reduce la complejidad para mantener aplicaciones
- Colaboración entre el equipo de Desarrollo y Operaciones

### Herramientas
- Jenkins
- TravisCI
- Bamboo
- CircleCI
- GitLab
- Github Actions
- Azure DevOps

#### Jenkins
Es una herramienta de CI basada en Java, que se puede usar como servidor CI o CD hub para un proyecto. Puede encargarse de la distribución, así como en distintas herramientas.
Pasos generales de la implementación con Jenkins son:
- Code & Commit: Usando IDE para crear código (VSCode) y luego se envía a una herramienta de versionamiento como Git.
- Build & Config: Se construye con compliadore, como Docker, o entornos de cómputo.
- Scan & Test: Se usan herramientas de escaneo y testeo como JUnit, Sonar, etc
- Release: Se despliega con herramientas para despliegue.
- Deploy: Se usan herramientas como VMWare, Azure, AWS, Docker, Kubernetes.
Cada vez que se corre un despliegue e integración, se da un estatus de salud y calidad del build.
  

