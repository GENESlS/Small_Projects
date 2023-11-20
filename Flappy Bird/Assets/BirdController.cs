using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BirdController : MonoBehaviour
{
    public float flapForce = 5f;
    public float forwardSpeed = 2f;
    public float rotationMultiplier = 2f;

    private Rigidbody2D rb;
   // private bool isDead = false;
    private bool hasStarted;
    public bool isGameOver;
    public int playerScore = 0;

    public GameObject endScreen, a, b;

    private void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        hasStarted = false;
       // rb.velocity = new Vector2(forwardSpeed, 0f);
        rb.isKinematic = true;
    }

    private void Update()
    {
       /* if (Input.GetKeyDown(KeyCode.Space) && !isDead)
        {
            Flap(); 
        } */
        if (!isGameOver)
        {
            if (!hasStarted && (Input.GetButtonDown("Jump") || Input.GetMouseButtonDown(0)))
            {
                hasStarted = true;
                a.SetActive(true);
                rb.isKinematic = false;
            }

            if (hasStarted && (Input.GetButtonDown("Jump") || Input.GetMouseButtonDown(0)))
            {
                rb.velocity = Vector2.zero;
                rb.AddForce(new Vector2(0, flapForce));
            }
        } else GameOver();
    }

    void FixedUpdate()
    {
        if (hasStarted && !isGameOver)
        {
            if (Time.deltaTime > 0) forwardSpeed = forwardSpeed + (Time.deltaTime*0.1f);
            rb.velocity = new Vector2(forwardSpeed, rb.velocity.y);
            UpdateRotation();
        }
    }

    void UpdateRotation()
    {
        float rotationZ = rb.velocity.y * rotationMultiplier;
        rotationZ = Mathf.Clamp(rotationZ, -90f, 45f);
        transform.rotation = Quaternion.Euler(0, 0, rotationZ);
    }

    public bool HasStarted()
    {
        return hasStarted;
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "DeathZone")
        {
            isGameOver = true;
        }
        if (other.tag == "ScoreZone")
        {
            playerScore++;
        }
    }

    void OnCollisionEnter2D(Collision2D other)
    {
        if (other.transform.tag == "DeathZone")
        {
            isGameOver = true;
        }
    }

    void GameOver()
    {
        endScreen.SetActive(true);
        GetComponent<BirdController>().enabled = false;
        b.GetComponent<CameraFollowNew>().enabled = false;
        a.GetComponent<ObstacleSpawner>().enabled = false;
    }

/*
    private void Flap()
    {
        rb.velocity = new Vector2(rb.velocity.x, flapForce);
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Pipe") || collision.gameObject.CompareTag("Ground"))
        {
            GameOver();
        }
    }

    private void GameOver()
    {
        isDead = true;
        // Add code to handle game over logic (e.g., display game over screen, stop the game).
    } */
}
