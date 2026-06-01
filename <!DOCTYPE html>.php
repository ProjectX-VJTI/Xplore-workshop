<!DOCTYPE html>
<html lang="en">

<head>
<title>CSS Grid Image Gallery</title>

<style>

body{
margin:0;
padding:20px;
font-family:Arial, sans-serif;
}

.gallery{
display:grid;
width:90%;
margin:auto;
grid-template-columns:repeat(8,1fr);
grid-template-rows:repeat(10,10vw);
gap:10px;
}

.gallery figure{
margin:0;
}

.gallery_img{
width:100%;
height:100%;
object-fit:cover;
display:block;
}

.gallery_item1{
grid-column:1 / 3;
grid-row:1 / 3;
}

.gallery_item2{
grid-column:3 / 5;
grid-row:1 / 3;
}

.gallery_item3{
grid-column:5 / 9;
grid-row:1 / 6;
}

.gallery_item4{
grid-column:1 / 5;
grid-row:3 / 6;
}

.gallery_item5{
grid-column:1 / 5;
grid-row:6 / 9;
}

.gallery_item6{
grid-column:5 / 9;
grid-row:6 / 9;
}

.gallery_item7{
grid-column:1 / 3;
grid-row:9 / 11;
}

.gallery_item8{
grid-column:3 / 6;
grid-row:9 / 11;
}

.gallery_item9{
grid-column:6 / 9;
grid-row:9 / 11;
}

</style>
</head>


<body>

<div class="gallery">

<figure class="gallery_item1">
<img src="https://images.pexels.com/photos/814499/pexels-photo-814499.jpeg" class="gallery_img">
</figure>

<figure class="gallery_item2">
<img src="https://images.pexels.com/photos/3857215/pexels-photo-3857215.jpeg" class="gallery_img">
</figure>

<figure class="gallery_item3">
<img src="https://images.pexels.com/photos/1933319/pexels-photo-1933319.jpeg" class="gallery_img">
</figure>

<figure class="gallery