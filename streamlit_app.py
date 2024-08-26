import streamlit as st
from PIL import Image
import io

def resize_image(image, width, height):
    # Use LANCZOS filter for high-quality resizing
    return image.resize((width, height), Image.LANCZOS)

def main():
    st.title("Image Resizer")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Open image
        image = Image.open(uploaded_file)
        
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Resize options
        st.sidebar.header("Resize Options")
        width = st.sidebar.number_input("Width", min_value=1, value=image.width)
        height = st.sidebar.number_input("Height", min_value=1, value=image.height)
        
        # Resize image
        resized_image = resize_image(image, width, height)
        
        # Show resized image
        st.subheader("Resized Image")
        st.image(resized_image, caption="Resized Image", use_column_width=True)
        
        # Save resized image to BytesIO object
        buffered = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        
        # Download button
        st.sidebar.download_button(
            label="Download Resized Image",
            data=img_bytes,
            file_name="resized_image.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
