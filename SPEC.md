# Slider Gallery Project Specification

## Project Overview
- **Project name**: Slider Gallery
- **Type**: Django web application
- **Core functionality**: Photo gallery with synced slider and lightbox functionality
- **Target users**: Website administrators managing slider content via Django admin

## Technical Stack
- Python 3.12
- Django 5.2
- MySQL
- Bootstrap 5
- Slick Slider
- django-filer (image management)
- django-admin-sortable2 (drag&drop ordering)

## UI/UX Specification

### Layout Structure
- Header: Simple navigation bar
- Main content: Full-width synced slider (main photo + thumbnails)
- Footer: Simple footer

### Visual Design
- Bootstrap 5 color scheme
- Clean, minimal design
- Responsive breakpoints (mobile, tablet, desktop)

### Components
1. **Main Slider** (Slick Slider - Syncing mode)
   - Large image display (foremost)
   - Thumbnail navigation below
   
2. **Lightbox Gallery**
   - Opens on main image click
   - Full-screen image viewing
   - Arrow navigation between images
   - Close button

3. **Django Admin**
   - SliderItem model management
   - Drag&drop ordering
   - Image preview in list
   - Russian language interface

## Functionality Specification

### Core Features
1. Slider displays images from database
2. Thumbnail navigation syncs with main image
3. Click on main image opens lightbox
4. Lightbox supports keyboard navigation (arrows, escape)
5. Admin interface for managing slider items
6. Drag&drop reordering in admin

### Data Model
- **SliderItem**
  - title (CharField, Russian label: "Название")
  - image (FilerImageField)
  - order (PositiveIntegerField for sorting)

## Acceptance Criteria
- [ ] Django project runs without errors
- [ ] MySQL database connected
- [ ] Slider displays images from database
- [ ] Slick Slider syncing works correctly
- [ ] Lightbox opens on image click
- [ ] Admin shows image thumbnails
- [ ] Drag&drop sorting works in admin
- [ ] All labels in Russian
- [ ] Dependencies in req.pip
