# Modelos 3D de demonstração

Além de qualquer arquivo `.glb` ou `.gltf` enviado a esta pasta, o build do Render baixa três modelos gratuitos de demonstração para a estante Props:

- **Fox** (`fox-character.glb`): personagem raposa com animações Survey, Walk e Run.
- **Car Concept** (`car-concept.glb`): carro conceitual.
- **Cesium Milk Truck** (`cesium-milk-truck.glb`): caminhão de leite com animação das rodas.

Os arquivos são obtidos durante o build, de uma revisão fixa do repositório [Khronos glTF Sample Assets](https://github.com/KhronosGroup/glTF-Sample-Assets). Assim não é preciso enviar os binários grandes para o Git do IronTool. O Render precisa ter acesso à internet durante o build. Abra a estante Props na aplicação para apresentar os modelos.

## Créditos e licenças dos modelos

- **Fox**: modelo original por PixelMannen (CC0-1.0); rig/animações por tomkranis (CC BY 4.0); conversão glTF por @AsoboStudio e @scurest (CC BY 4.0). A licença CC BY exige atribuição. [Créditos e licença no repositório de origem](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/e124e8d8d7330a5372bc2b4d00d39a4d9d7997ea/Models/Fox).
- **Car Concept**: modelo e texturas por Eric Chadwick / Darmstadt Graphics Group GmbH (CC BY 4.0); baseado em modelo CC0 de Unity Fan. [Créditos e licença no repositório de origem](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/e124e8d8d7330a5372bc2b4d00d39a4d9d7997ea/Models/CarConcept).
- **Cesium Milk Truck**: modelo por Cesium (CC BY 4.0). O crédito não implica endosso pela Cesium; marcas e logotipos são excluídos da licença do modelo. [Créditos e licença no repositório de origem](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/e124e8d8d7330a5372bc2b4d00d39a4d9d7997ea/Models/CesiumMilkTruck).

Para incluir mais modelos próprios, coloque arquivos `.glb` ou `.gltf` aqui e envie um commit. O build copia `media/` para a aplicação; o Render fará o deploy automático. Para hologramas, use `media/holo/`. Confira sempre a licença e os créditos de cada modelo antes de redistribuí-lo.
