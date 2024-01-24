def predict(image):
    # Definimos las transformaciones que se deben aplicar a la imagen para que coincida con el formato MNIST
    transformations = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    # Aplicamos las transformaciones a la imagen
    img_transformed = transformations(image)
    
    # Convertimos la imagen para que tenga una dimensión de lote (que PyTorch espera)
    img_batch = img_transformed.unsqueeze(0)  # Agrega un batch dimension en la posición 0
    
    # Verificamos las ...
    # (Continue your code here, as the last line is incomplete)
