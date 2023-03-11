# DevOps Engineering

<font size=1>
    Basado en el curso de <a href=https://www.youtube.com/watch?v=j5Zsa_eOXeY&ab_channel=freeCodeCamp.org>
    FreeCode Camp - DevOps Engineering
    </a>
</font>

----




## 1. Definición

![img](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2021/07/13429_ILL_DevOpsLoop.png)
Es una metodología que ayuda a los equipos de ingeniería a conmstruir productos, mientras se tiene feedback constante del usuario.
Ciclo continuo de `Planear // Codificar // Construir // Testear // Release // Desplegar // Operar // Monitor`

- **1.1. Ingeniería DevOps:** Persona encargada de construir, testear, release y monitorar aplicaciones. Se encargan de automatizar:
  - _Pull Request:_ Al compartir cambios en el código usando herramientas git (Gitlab, GitHub), se envía un pull request para integrar los cambios dentro del código actual. Esto se da a través de un `Code Review`.
  - _Despliegues:_ Se puede automatizar CI, Cambios de ambientes efímeros, escaneos de seguridad, y notificaciones a revisores. La idea es que todo pueda ser integrado a la base del código dentro de las 24 horas después de proponer cambios. Distribuir caracteríticas solo a ciertos usuarios antes de hacer despliegues públicos, inicializar nuevos servicios sin downtime, rollbacks.
  - _Administración del rendimiento de la aplicación:_ Métricas, logging, Monitoreo, Alertas.
  - __Meta:__ Tener las herramientas adecuadas en lugar para facilitar el desarrollo sin tener mucho código personalizado.

## 2. Test Driven Development (TDD)





