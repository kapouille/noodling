window.onload = ->
  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 )
  camera.position.z = 5

  renderer = new THREE.WebGLRenderer()
  renderer.setSize( window.innerWidth, window.innerHeight )
  document.body.appendChild(renderer.domElement)

  material = new THREE.MeshBasicMaterial
    color: 0x00ff00
    wireframe: true
  inner = new THREE.Mesh(new THREE.RingGeometry(0, 1.5, 8, 1), material)
  scene.add(inner)
  outer = new THREE.Mesh(new THREE.RingGeometry(0, 3, 8, 1), material)
  scene.add(outer)

  render = ->
    requestAnimationFrame(render)
    rotation = inner.rotation
    rotation.x += 0.01
    rotation.y += 0.01
    rotation = outer.rotation
    rotation.x += 0.01
    rotation.y += 0.01

    renderer.render(scene, camera)

  render()
