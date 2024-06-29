using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EndlessRoad : MonoBehaviour
{
    private Rigidbody2D bg;

    public Vector2 startPosition;
    public float scrollSpeed = 2f;
    // Start is called before the first frame update
    private void Start()
    {
        bg = gameObject.GetComponentInChildren<Rigidbody2D>();
        startPosition = transform.position;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        transform.Translate(Vector3.left * scrollSpeed * Time.deltaTime);
        //Debug.Log("Background position: " + transform.position);
    }
}
