
/**
 * \brief Renders the whole scene with a specified rendering context.
 *
 * All the camera-specific calls to glRotatef/glTranslatef should already
 * be called before calling this function. For possible methods to set up
 * the scene to be ready for rendering, refer to \ref grp_SetupScene.
 *
 * \param ctx Rendering context.
 * \param cam The camera from which the rendering is performed.
 *
 * \retval RenderStateNull An error has occured while rendering.
 * \retval Otherwise       A valid render state suitable for reuse
 *                         (whatever that means).
 */
RenderState render (Context const& ctx, Camera const& cam);

