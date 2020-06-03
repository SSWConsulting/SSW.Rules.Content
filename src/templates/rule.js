import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';
import {
  faThumbsUp,
  faThumbsDown
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
export default function Rule({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) {
  const rule = data.markdownRemark;
  return (
    <Layout
      crumbs={crumbs}
      crumbLabel={rule.frontmatter.title}
      displayActions={false}
    >
      <div className="rule-single rounded">
        <section className="rule-content p-12 mb-12">
          <h1>{rule.frontmatter.title}</h1>
          <small>
            Created on {rule.frontmatter.created} | Last updated by{' '}
            <a href="/profile">{rule.frontmatter.authors[0].title}</a>{' '}
            {rule.frontmatter.created}
          </small>
          <hr />
          <div dangerouslySetInnerHTML={{ __html: rule.html }} />

          <section id="more" className="pt-12 mt-12 flex text-center">
            <div className="acknowledgements w-1/3">
              <h5>Acknowledgements</h5>
              <div className="avatar">
                <a href="/profile">
                  <img
                    className="rounded-full inline"
                    src="https://adamcogan.com/wp-content/uploads/2018/07/adam-bw.jpg"
                    alt="Adam Cogan"
                  />
                </a>
              </div>
            </div>
            <div className="tags rounded w-1/3">
              <h5>Tags</h5>
              <span>Scrum</span> <span>Some other tag</span>{' '}
              <span>One more</span> <span>And another</span>
            </div>
            <div className="likes w-1/3">
              <h5>Feedback</h5>
              <p>
                <span>
                  8 <FontAwesomeIcon icon={faThumbsUp} className="good" />
                </span>{' '}
                <span>
                <FontAwesomeIcon icon={faThumbsDown} className="bad" /> 2
                </span>
              </p>
              <p>
                <small>
                  <a href="/suggestion">Make a suggestion</a>
                </small>
              </p>
            </div>
          </section>
        </section>
      </div>
    </Layout>
  );
}

Rule.propTypes = {
  data: PropTypes.object.isRequired,
  pageContext: PropTypes.object.isRequired,
};

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        authors {
          title
        }
        created(formatString: "DD MMM YYYY")
      }
    }
  }
`;
