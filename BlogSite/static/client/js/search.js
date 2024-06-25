$(document).ready(function() {
    let my_Categ_ids = [];
    let my_tags_ids = [];

    // Function to handle filtering based on current selections
    function filterPosts() {
        var searchText = $('#Search_input').val().toLowerCase();
    
        $('.post-container').each(function() {
            var postTitle = $(this).data('post_title').toLowerCase();
            var postContent = $(this).data('post_contain').toLowerCase();
            var postTags = $(this).data('post_tags'); // Array of tags
            var postCategories = $(this).data('post_categories'); // Array of categories
    
            // Check if either post title or content contains the search text
            var titleMatch = postTitle.includes(searchText);
            var contentMatch = postContent.includes(searchText);
    
            // Check if any of the post's tags match the selected ones
            var tagsMatch = my_tags_ids.length === 0 || postTags.some(tag => my_tags_ids.includes(tag.toString()));
    
            // Check if any of the post's categories match the selected ones
            var categoriesMatch = my_Categ_ids.length === 0 || postCategories.some(category => my_Categ_ids.includes(category.toString()));
    
            if ((searchText === '' || titleMatch || contentMatch) && tagsMatch && categoriesMatch) {
                $(this).show(); // Display the post if it matches
            } else {
                $(this).hide(); // Hide the post if it doesn't match
            }
        });
    }
    

    // Handle input in the search field
    $('#Search_input').on('input', function() {
        filterPosts();
    });

    // Handle changes in category checkboxes
    $(document).on('change', 'input[name="categories"]', function() {
        let categoryId = $(this).data("categories").toString();

        if ($(this).prop('checked')) {
            // Checkbox is checked
            if (!my_Categ_ids.includes(categoryId)) {
                my_Categ_ids.push(categoryId);
            }
        } else {
            // Checkbox is unchecked
            let index = my_Categ_ids.indexOf(categoryId);
            if (index !== -1) {
                my_Categ_ids.splice(index, 1);
            }
        }

        filterPosts();
    });

    // Handle changes in tag checkboxes
    $(document).on('change', 'input[name="tags"]', function() {
        let tagId = $(this).data("tags").toString();

        if ($(this).prop('checked')) {
            // Checkbox is checked
            if (!my_tags_ids.includes(tagId)) {
                my_tags_ids.push(tagId);
            }
        } else {
            // Checkbox is unchecked
            let index = my_tags_ids.indexOf(tagId);
            if (index !== -1) {
                my_tags_ids.splice(index, 1);
            }
        }

        filterPosts();
    });

    // Initial filter application
    filterPosts();
});




// version 1

// $(document).ready(function() {
//     let my_Categ_ids = [];
//     let my_tags_ids = [];

//     // Function to handle filtering based on current selections
//     function filterPosts() {
//         var searchText = $('#Search_input').val().toLowerCase();

//         $('.post-container').each(function() {
//             var postTitle = $(this).data('post_title').toLowerCase();
//             var postContent = $(this).data('post_contain').toLowerCase();
//             var postTags = $(this).data('post_tags').toString(); // Ensure tags are treated as string
//             var postCategories = $(this).data('post_categories').toString(); // Ensure categories are treated as string

//             // Check if either post title or content contains the search text
//             var titleMatch = postTitle.includes(searchText);
//             var contentMatch = postContent.includes(searchText);

//             // Check if the post's tags or categories match the selected ones
//             var tagsMatch = my_tags_ids.length === 0 || postTags.split(',').some(tag => my_tags_ids.includes(tag));
//             var categoriesMatch = my_Categ_ids.length === 0 || my_Categ_ids.includes(postCategories);

//             if ((searchText === '' || titleMatch || contentMatch) && tagsMatch && categoriesMatch) {
//                 $(this).show(); // Display the post if it matches
//             } else {
//                 $(this).hide(); // Hide the post if it doesn't match
//             }
//         });
//     }

//     // Handle input in the search field
//     $('#Search_input').on('input', function() {
//         filterPosts();
//     });

//     // Handle changes in category checkboxes
//     $(document).on('change', 'input[name="categories"]', function() {
//         let categoryId = $(this).data("categories").toString();

//         if ($(this).prop('checked')) {
//             // Checkbox is checked
//             if (!my_Categ_ids.includes(categoryId)) {
//                 my_Categ_ids.push(categoryId);
//             }
//         } else {
//             // Checkbox is unchecked
//             let index = my_Categ_ids.indexOf(categoryId);
//             if (index !== -1) {
//                 my_Categ_ids.splice(index, 1);
//             }
//         }

//         filterPosts();
//     });

//     // Handle changes in tag checkboxes
//     $(document).on('change', 'input[name="tags"]', function() {
//         let tagId = $(this).data("tags").toString();

//         if ($(this).prop('checked')) {
//             // Checkbox is checked
//             if (!my_tags_ids.includes(tagId)) {
//                 my_tags_ids.push(tagId);
//             }
//         } else {
//             // Checkbox is unchecked
//             let index = my_tags_ids.indexOf(tagId);
//             if (index !== -1) {
//                 my_tags_ids.splice(index, 1);
//             }
//         }

//         filterPosts();
//     });

//     // Initial filter application
//     filterPosts();
// });
