# Graphics Final Project
### Jen Yu and Shannon Lau (pd 4 Graphics)

## Features Implemented
 1. Ambient Light
  * Allows MDL programmer to set the ambient light
  * Function call: `ambient red green blue`
  * Example: ` ambient 50 50 50`
 2. Light
  * Allows MDL programmer to define different sources of light
  * Can set the x, y, z coordinate and the RGB value of the light color
  * Function call: `light x y z red green blue`
  * Example: ` light 0 0 0 255 0 0`
 3. Constants
  * Allows MDL programmer to create the lighting constants
  * Define constants based on ambient, diffuse and specular
  * Function call: ` constants [name] ambientR diffuseR specularR ambientG diffuseG specularG ambientB diffuseB specularB`
  * Example: `constants lights 0.1 0.2 0.3 0.1 0.2 0.3 0.1 0.2 0.3`
