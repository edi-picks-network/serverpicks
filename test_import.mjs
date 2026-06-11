// Test script to check if BLOG_POSTS imports correctly
import { BLOG_POSTS } from '../app/data/blog-posts.js';
console.log('Blog posts count:', BLOG_POSTS.length);
BLOG_POSTS.forEach(p => console.log('-', p.slug, p.title?.substring(0, 40)));
