import React, { useRef } from 'react';
import { graphql, Link } from "gatsby";
import Layout from '../components/layout/layout';
export default function Category({ data, 
    pageContext: {
      breadcrumb: { crumbs },
    } 
  }) {
  
  const linkRef = useRef();
  const post = data.markdownRemark
  return (
    <Layout crumbs={crumbs} displayActions={false}>
        <div>
        <h1>{post.frontmatter.title}</h1>
        <div dangerouslySetInnerHTML={{ __html: post.html }} />
      </div>
      <ol className="list-decimal list-inside">
       { data.rule.nodes.map((element, i) => 
        <li key={i}>
            {' '}
            <Link ref={linkRef} to={`/${element.frontmatter.folder}`}>
            {element.frontmatter.title}
            </Link>
        </li>
        )}
        </ol>
    </Layout>
  )
}
export const query = graphql`
  query($slug: String!, $index: [String]!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
      }
    },
    rule: allMarkdownRemark(filter: {frontmatter: {folder: {in: $index}}}) {
        nodes {
            frontmatter {
              folder
              title
            }
            html
          }
        }
      }
`